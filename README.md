# AI Context

Centralized AI context management for multiple AI assistants (Copilot, Gemini, Cursor, etc.).

## 📁 Structure

```
~/.ai-context/
├── rules/          # ALWAYS rules (applied to every response)
│   └── ALWAYS.md   # Main instructions file
├── skills/         # Reusable skill definitions
├── agents/         # Agent configurations
├── workflows/      # Workflow orchestrations
└── scripts/        # CLI tools
    ├── aictx        # Main CLI (Python)
    ├── aictx.sh     # Shell wrapper
    └── install.sh  # Setup script
```

## 🚀 Quick Start

### 1. Install the CLI

```bash
cd ~/.ai-context/scripts
./install.sh
```

This adds `aictx` to your PATH and sets `AICTX_HOME`.

### 2. Configure AI Tools

```bash
# Interactive installation
aictx install

# Or install everything at once
aictx install --all -y
```

### 3. Check Status

```bash
aictx status
```

## 📋 Commands

| Command | Description |
|---------|-------------|
| `aictx install` | Interactive installation of links |
| `aictx install --all` | Install all resources to all targets |
| `aictx install -f` | Force overwrite existing links |
| `aictx status` | Show current link status |
| `aictx uninstall` | Remove all created links |
| `aictx config` | Show configuration info |

## 🎯 Supported AI Tools

- **VS Code / GitHub Copilot** (`~/.vscode/copilot-instructions.md`)
- **Google Gemini** (`~/.gemini/antigravity/`)
- **GitHub** (`~/.github/copilot-instructions.md`)
- **Cursor IDE** (`~/.cursor/`)
- **Windsurf IDE** (`~/.windsurf/`)
- **Sourcegraph Cody** (`~/.cody/`)

## 🔧 Manual Setup

If you prefer manual configuration:

```bash
# Add to ~/.bashrc or ~/.zshrc
export AICTX_HOME="$HOME/.ai-database"
export PATH="$AICTX_HOME/scripts:$PATH"
```

## 📖 How It Works

The CLI creates symbolic links from your AI database to each tool's config directory:

- **Instructions targets** (Copilot, GitHub): Links `rules/ALWAYS.md` → `copilot-instructions.md`
- **Folder targets** (Gemini, Cursor): Links entire `skills/`, `agents/`, etc. folders

This means you maintain a single source of truth, and all AI tools share the same context.
