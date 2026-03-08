#!/bin/bash
#
# AI Context - Quick Setup Script
# 
# This script sets up the aidb CLI tool for easy access.
# Run it once to configure your shell environment.
#
# Usage:
#   ./install.sh
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Determine script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
AICTX_HOME="$(dirname "$SCRIPT_DIR")"

echo -e "${CYAN}${BOLD}"
echo "═══════════════════════════════════════════════════════════"
echo "  AI Context - Setup"
echo "═══════════════════════════════════════════════════════════"
echo -e "${NC}"

echo -e "  ${BLUE}ℹ${NC} AI Context: $AICTX_HOME"
echo ""

# Make scripts executable
chmod +x "$SCRIPT_DIR/aictx"
chmod +x "$SCRIPT_DIR/aictx.sh"
echo -e "  ${GREEN}✓${NC} Made scripts executable"

# Detect shell
SHELL_NAME=$(basename "$SHELL")
case "$SHELL_NAME" in
    zsh)
        RC_FILE="$HOME/.zshrc"
        ;;
    bash)
        if [[ -f "$HOME/.bashrc" ]]; then
            RC_FILE="$HOME/.bashrc"
        else
            RC_FILE="$HOME/.bash_profile"
        fi
        ;;
    *)
        RC_FILE="$HOME/.profile"
        ;;
esac

echo -e "  ${BLUE}ℹ${NC} Detected shell: $SHELL_NAME"
echo -e "  ${BLUE}ℹ${NC} Config file: $RC_FILE"
echo ""

# Check if already configured
if grep -q "AICTX_HOME" "$RC_FILE" 2>/dev/null; then
    echo -e "  ${YELLOW}⚠${NC} AICTX_HOME already configured in $RC_FILE"
    echo ""
    read -p "  Update existing configuration? [y/N]: " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "  ${BLUE}ℹ${NC} Skipping shell configuration."
    else
        # Remove old configuration
        sed -i.bak '/# AI Context/d' "$RC_FILE"
        sed -i.bak '/AICTX_HOME/d' "$RC_FILE"
        ADD_CONFIG=true
    fi
else
    ADD_CONFIG=true
fi

# Add configuration to shell RC file
if [[ "$ADD_CONFIG" == "true" ]]; then
    echo "" >> "$RC_FILE"
    echo "# AI Context CLI" >> "$RC_FILE"
    echo "export AICTX_HOME=\"$AICTX_HOME\"" >> "$RC_FILE"
    echo "export PATH=\"\$AICTX_HOME/scripts:\$PATH\"" >> "$RC_FILE"
    echo -e "  ${GREEN}✓${NC} Added configuration to $RC_FILE"
fi

echo ""
echo -e "${BOLD}Setup Complete!${NC}"
echo ""
echo "  To start using aidb, either:"
echo ""
echo "  1. Restart your terminal, or"
echo "  2. Run: source $RC_FILE"
echo ""
echo "  Then run:"
echo "    aictx install    # Configure AI tool links"
echo "    aictx status     # Check current status"
echo "    aictx --help     # Show all commands"
echo ""
