# AICTX Control Center (Web UI)

A local (localhost-only) web UI layer for the `aictx` CLI.

## Goals

- Provide a clear visual interface to run the existing `aictx` commands
- Stream-like UX via polling (STDOUT/STDERR updates while commands run)
- Safe by default:
  - binds to `127.0.0.1`
  - no shell execution (argv list only)
  - strict command whitelist
  - blocks interactive TUI/prompt flows unless required args are provided

## How to run

### Option A: Launcher script

```bash
cd ~/.ai-context
./scripts/aictx-web --port 8787
```

If you get a permissions error:

```bash
cd ~/.ai-context
chmod +x scripts/aictx-web
./scripts/aictx-web --port 8787
```

### Option B: Run the backend directly

```bash
cd ~/.ai-context
python3 stitch_aictx_control_center/control_center/backend/server.py --port 8787
```

Then open:

- http://127.0.0.1:8787

## Notes

- Command history and logs are stored under:
  - `~/.ai-context/.aictx-web/runs/<runId>/`
- For web mode, the backend rejects interactive flows:
  - `install` requires `--all` or `--targets`
  - `uninstall` requires `--targets` and `--yes`
  - `add` requires `kind` and `name`
  - `context` requires an `action`
  - `archive` / `unarchive` require `kind` and `name`

## Development

Static frontend files live in:
- `stitch_aictx_control_center/control_center/web/`

Backend server:
- `stitch_aictx_control_center/control_center/backend/server.py`
