#!/usr/bin/env python3
"""AICTX Control Center — local web backend.

This server runs on localhost and provides a safe API wrapper around the
existing `aictx` CLI.

Goals:
- Localhost-only (binds to 127.0.0.1)
- No shell execution (argv list only)
- Strict command whitelist
- Non-interactive only: commands that would open TUI/prompts are rejected unless
  explicit args are provided.

Run:
  python3 stitch_aictx_control_center/control_center/backend/server.py --port 8787
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import subprocess
import threading
import time
import uuid
from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
from urllib.parse import parse_qs, unquote, urlparse

ANSI_ESCAPE_RE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

ALLOWED_COMMANDS = {
    "test",
    "sync",
    "doctor",
    "context",
    "add",
    "archive",
    "unarchive",
    "archived",
    "skills-scripts",
    "skillscripts",
    "run-skill",
    "status",
    "uninstall",
    "config",
    "agents",
    "audit",
    "ls",
    "init",
    "install",
    "telemetry",
}

MUTATING_COMMANDS = {
    "sync",
    "install",
    "uninstall",
    "archive",
    "unarchive",
    "doctor",  # may be mutating if --fix
    "context",
    "add",
    "init",
}


def strip_ansi(text: str) -> str:
    return ANSI_ESCAPE_RE.sub("", text)


def find_aictx_home(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "scripts" / "aictx").exists():
            return candidate
    raise RuntimeError("Could not locate AICTX_HOME (expected scripts/aictx)")


@dataclass
class RunState:
    run_id: str
    argv: list[str]
    started_at: float
    finished_at: Optional[float]
    status: str
    pid: Optional[int]
    return_code: Optional[int]
    stdout_path: Path
    stderr_path: Path

    def to_public_json(self) -> Dict[str, Any]:
        finished_at = self.finished_at
        duration_ms = None
        if finished_at is not None:
            duration_ms = int((finished_at - self.started_at) * 1000)
        return {
            "runId": self.run_id,
            "argv": self.argv,
            "status": self.status,
            "pid": self.pid,
            "returnCode": self.return_code,
            "startedAt": self.started_at,
            "finishedAt": finished_at,
            "durationMs": duration_ms,
        }


class RunStore:
    def __init__(self, root_dir: Path) -> None:
        self.root_dir = root_dir
        self.runs_dir = root_dir / "runs"
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        self._runs: Dict[str, RunState] = {}
        self._lock = threading.Lock()
        self._mutating_lock = threading.Lock()

    def _run_dir(self, run_id: str) -> Path:
        return self.runs_dir / run_id

    def create_run(self, argv: list[str], mutating: bool) -> RunState:
        if mutating:
            acquired = self._mutating_lock.acquire(blocking=False)
            if not acquired:
                raise RuntimeError("Another mutating run is already in progress")

        run_id = uuid.uuid4().hex
        run_dir = self._run_dir(run_id)
        run_dir.mkdir(parents=True, exist_ok=True)
        stdout_path = run_dir / "stdout.txt"
        stderr_path = run_dir / "stderr.txt"

        state = RunState(
            run_id=run_id,
            argv=argv,
            started_at=time.time(),
            finished_at=None,
            status="running",
            pid=None,
            return_code=None,
            stdout_path=stdout_path,
            stderr_path=stderr_path,
        )

        with self._lock:
            self._runs[run_id] = state

        self._write_meta(state)
        return state

    def finish_run(self, run_id: str, return_code: int, mutating: bool) -> None:
        with self._lock:
            state = self._runs.get(run_id)
            if not state:
                return
            state.status = "finished"
            state.finished_at = time.time()
            state.return_code = return_code
            self._write_meta(state)

        if mutating:
            try:
                self._mutating_lock.release()
            except RuntimeError:
                pass

    def set_pid(self, run_id: str, pid: int) -> None:
        with self._lock:
            state = self._runs.get(run_id)
            if not state:
                return
            state.pid = pid
            self._write_meta(state)

    def get(self, run_id: str) -> Optional[RunState]:
        with self._lock:
            return self._runs.get(run_id)

    def _write_meta(self, state: RunState) -> None:
        meta_path = self._run_dir(state.run_id) / "meta.json"
        meta_path.write_text(json.dumps(state.to_public_json(), indent=2))


def validate_non_interactive(argv: list[str]) -> None:
    if not argv:
        raise ValueError("argv is required")
    command = argv[0]

    if command not in ALLOWED_COMMANDS:
        raise ValueError(f"Command not allowed: {command}")

    # Prevent launching the CLI's interactive TUIs/prompts in a web context.
    if command == "install":
        if "--all" not in argv and "--targets" not in argv:
            raise ValueError("install requires --all or --targets in web mode")

    if command == "uninstall":
        if "--targets" not in argv:
            raise ValueError("uninstall requires --targets in web mode")

    if command == "add":
        # Expected: add <skill|agent> <name> ...
        if len(argv) < 3:
            raise ValueError("add requires kind and name in web mode")

    if command == "context":
        # Expected: context <enable|disable|toggle|status>
        if len(argv) < 2:
            raise ValueError("context requires an action in web mode")

    if command in ("archive", "unarchive"):
        if len(argv) < 3:
            raise ValueError(f"{command} requires kind and name in web mode")


def read_json_file(path: Path) -> Tuple[int, Dict[str, Any]]:
    if not path.exists():
        return HTTPStatus.NOT_FOUND, {"ok": False, "error": f"Not found: {path.name}"}
    try:
        return HTTPStatus.OK, json.loads(path.read_text())
    except Exception as e:
        return HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "error": str(e)}


class ControlCenterHandler(BaseHTTPRequestHandler):
    server_version = "AICTXControlCenter/0.1"

    def log_message(self, format: str, *args: Any) -> None:
        # Keep stdout clean; this server is intended to be used locally.
        return

    @property
    def aictx_home(self) -> Path:
        return self.server.aictx_home  # type: ignore[attr-defined]

    @property
    def web_root(self) -> Path:
        return self.server.web_root  # type: ignore[attr-defined]

    @property
    def run_store(self) -> RunStore:
        return self.server.run_store  # type: ignore[attr-defined]

    @property
    def aictx_script(self) -> Path:
        return self.server.aictx_script  # type: ignore[attr-defined]

    def _json_response(self, status: int, payload: Dict[str, Any]) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_json_body(self) -> Dict[str, Any]:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        raw = self.rfile.read(length) if length > 0 else b"{}"
        return json.loads(raw.decode("utf-8"))

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/manifest":
            status, payload = read_json_file(self.aictx_home / ".aictx-manifest.json")
            self._json_response(status, payload)
            return

        if path == "/api/context-sizes":
            status, payload = read_json_file(self.aictx_home / ".context-sizes.json")
            self._json_response(status, payload)
            return

        if path == "/api/state":
            status, payload = read_json_file(self.aictx_home / ".aictx_state.json")
            self._json_response(status, payload)
            return

        if path.startswith("/api/run/"):
            run_id = path.split("/api/run/", 1)[1]
            state = self.run_store.get(run_id)
            if not state:
                self._json_response(HTTPStatus.NOT_FOUND, {"ok": False, "error": "Unknown runId"})
                return

            qs = parse_qs(parsed.query)
            stdout_offset = int(qs.get("stdoutOffset", ["0"])[0])
            stderr_offset = int(qs.get("stderrOffset", ["0"])[0])

            stdout_chunk, stdout_new_offset = self._read_file_chunk(state.stdout_path, stdout_offset)
            stderr_chunk, stderr_new_offset = self._read_file_chunk(state.stderr_path, stderr_offset)

            payload = {
                "ok": True,
                "run": state.to_public_json(),
                "stdout": {"offset": stdout_new_offset, "chunk": stdout_chunk},
                "stderr": {"offset": stderr_new_offset, "chunk": stderr_chunk},
            }
            self._json_response(HTTPStatus.OK, payload)
            return

        # Static content
        self._serve_static(path)

    def _read_file_chunk(self, path: Path, offset: int) -> Tuple[str, int]:
        if not path.exists():
            return "", offset
        data = path.read_bytes()
        if offset < 0:
            offset = 0
        if offset >= len(data):
            return "", len(data)
        chunk = data[offset:]
        # Decode with replacement to avoid breaking the UI on odd bytes
        text = chunk.decode("utf-8", errors="replace")
        return text, len(data)

    def _serve_static(self, request_path: str) -> None:
        safe_path = request_path
        if safe_path == "/":
            safe_path = "/index.html"

        safe_path = unquote(safe_path)
        if ".." in safe_path:
            self.send_error(HTTPStatus.BAD_REQUEST)
            return

        target = (self.web_root / safe_path.lstrip("/")).resolve()
        try:
            target.relative_to(self.web_root)
        except ValueError:
            self.send_error(HTTPStatus.FORBIDDEN)
            return

        if not target.exists() or not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        content = target.read_bytes()
        content_type, _ = mimetypes.guess_type(str(target))
        content_type = content_type or "application/octet-stream"

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8" if content_type.startswith("text/") else content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/run":
            try:
                payload = self._read_json_body()
            except Exception:
                self._json_response(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "Invalid JSON"})
                return

            argv = payload.get("argv")
            if not isinstance(argv, list) or not all(isinstance(x, str) for x in argv):
                self._json_response(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "argv must be a list of strings"})
                return

            argv = [a for a in argv if a != ""]
            if not argv:
                self._json_response(HTTPStatus.BAD_REQUEST, {"ok": False, "error": "argv must not be empty"})
                return

            try:
                validate_non_interactive(argv)
            except Exception as e:
                self._json_response(HTTPStatus.BAD_REQUEST, {"ok": False, "error": str(e)})
                return

            command = argv[0]
            mutating = command in MUTATING_COMMANDS
            try:
                state = self.run_store.create_run(argv=argv, mutating=mutating)
            except Exception as e:
                self._json_response(HTTPStatus.CONFLICT, {"ok": False, "error": str(e)})
                return

            threading.Thread(
                target=self._execute_run,
                args=(state.run_id, argv, mutating),
                daemon=True,
            ).start()

            self._json_response(
                HTTPStatus.CREATED,
                {
                    "ok": True,
                    "runId": state.run_id,
                    "runUrl": f"/api/run/{state.run_id}",
                    "pollIntervalMs": 500,
                },
            )
            return

        self.send_error(HTTPStatus.NOT_FOUND)

    def _execute_run(self, run_id: str, argv: list[str], mutating: bool) -> None:
        full_cmd = [
            os.environ.get("PYTHON", "python3"),
            str(self.aictx_script),
            *argv,
        ]

        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        env["AICTX_HOME"] = str(self.aictx_home)

        stdout_path = self.run_store.get(run_id).stdout_path  # type: ignore[union-attr]
        stderr_path = self.run_store.get(run_id).stderr_path  # type: ignore[union-attr]

        try:
            with open(stdout_path, "w", encoding="utf-8") as stdout_f, open(stderr_path, "w", encoding="utf-8") as stderr_f:
                proc = subprocess.Popen(
                    full_cmd,
                    cwd=str(self.aictx_home),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,
                    env=env,
                )

                self.run_store.set_pid(run_id, proc.pid)

                def pump(stream, sink, strip: bool) -> None:
                    if not stream:
                        return
                    for line in stream:
                        sink.write(strip_ansi(line) if strip else line)
                        sink.flush()

                t_out = threading.Thread(target=pump, args=(proc.stdout, stdout_f, True), daemon=True)
                t_err = threading.Thread(target=pump, args=(proc.stderr, stderr_f, True), daemon=True)
                t_out.start()
                t_err.start()

                rc = proc.wait()
                t_out.join(timeout=1)
                t_err.join(timeout=1)

                self.run_store.finish_run(run_id, rc, mutating=mutating)
        except Exception as e:
            try:
                stderr_path.write_text(f"Backend error: {e}\n")
            except Exception:
                pass
            self.run_store.finish_run(run_id, 1, mutating=mutating)


def build_server(host: str, port: int) -> ThreadingHTTPServer:
    here = Path(__file__).resolve()
    aictx_home = find_aictx_home(here)

    web_root = aictx_home / "stitch_aictx_control_center" / "control_center" / "web"
    if not web_root.exists():
        raise RuntimeError(f"web root not found: {web_root}")

    run_root = aictx_home / ".aictx-web"
    run_store = RunStore(run_root)

    httpd = ThreadingHTTPServer((host, port), ControlCenterHandler)
    httpd.aictx_home = aictx_home  # type: ignore[attr-defined]
    httpd.aictx_script = aictx_home / "scripts" / "aictx"  # type: ignore[attr-defined]
    httpd.web_root = web_root  # type: ignore[attr-defined]
    httpd.run_store = run_store  # type: ignore[attr-defined]
    return httpd


def main() -> int:
    parser = argparse.ArgumentParser(prog="aictx-control-center")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8787, help="Bind port (default: 8787)")
    args = parser.parse_args()

    httpd = build_server(args.host, args.port)
    print(f"AICTX Control Center running on http://{args.host}:{args.port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
