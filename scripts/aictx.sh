#!/bin/bash
#
# AI Context CLI - Shell wrapper
# This script provides a portable entry point for the aictx CLI tool.
#
# Usage:
#   ./aidb.sh install       # Interactive installation
#   ./aidb.sh status        # Show current link status
#   ./aidb.sh --help        # Show help
#

set -e

# Determine script directory (works on Linux, macOS, and most Unix-like systems)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"

# Set AICTX_HOME if not already set
export AICTX_HOME="${AICTX_HOME:-$(dirname "$SCRIPT_DIR")}"

# Check for Python 3
if command -v python3 &> /dev/null; then
    PYTHON="python3"
elif command -v python &> /dev/null; then
    # Check if python is Python 3
    if python --version 2>&1 | grep -q "Python 3"; then
        PYTHON="python"
    else
        echo "Error: Python 3 is required but not found."
        exit 1
    fi
else
    echo "Error: Python 3 is required but not found."
    exit 1
fi

# Run the Python script
exec "$PYTHON" "$SCRIPT_DIR/aictx" "$@"
