---
name: workspace-mapper
description: Maps all files in the current repository, collecting metadata (size, type, description) and saving it to `.ai-context/workspace-map.json`. Use this skill whenever the `workspace-guard` rule indicates the map is missing or when you need a precise overview of the project to locate files without slow manual searches.
---

# Workspace Mapper

This skill provides the ability to generate a structured repository map to assist in AI navigation and precision.

## When to use
- When the `.ai-context/workspace-map.json` file does not exist.
- After significant structural changes in the project (many files created or deleted).
- When you are uncertain about the location of a specific component or logic.

## Execution Flow
1. Execute the mapping script via Python.
2. The script will scan the current directory, ignoring irrelevant folders (`node_modules`, `.git`, etc.) and respecting `.gitignore`.
3. A JSON file will be generated at `.ai-context/workspace-map.json` with a line-indexed summary.

## Command
Run the following command in the terminal:
```bash
python3 /home/jonnathan/.ai-context/skills/workspace-mapper/scripts/mapper.py
```

## Output Structure
The generated file will follow this format:
```json
{
  "version": "1.3",
  "summary": {
    "total_files": 120,
    "line_guide": {
      "src/main.py": 150
    }
  },
  "files": [
    {
      "path": "src/main.py",
      "size_bytes": 1024,
      "type": "text/x-python",
      "description": "Python code."
    }
  ]
}
```

## Benefits
- **Precision**: Know exactly where each file is located without guessing.
- **Context Efficiency**: Instead of recursively listing directories, only read this JSON.
- **Line-Indexed Search**: Jump directly to file metadata using the `line_guide`.
