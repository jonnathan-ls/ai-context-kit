import os
import json
import mimetypes
import fnmatch
from datetime import datetime

def is_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk: return True
    except: return True
    return False

def load_gitignore_patterns(root_dir):
    patterns = []
    gitignore_path = os.path.join(root_dir, '.gitignore')
    if os.path.exists(gitignore_path):
        try:
            with open(gitignore_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'): patterns.append(line)
        except: pass
    return patterns

def should_exclude(name, path, root_dir, gitignore_patterns, exclude_dirs):
    if name in exclude_dirs: return True
    if name.startswith('.') and name != '.ai-context': return True
    rel_path = os.path.relpath(path, root_dir)
    for pattern in gitignore_patterns:
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(name, pattern): return True
    return False

def get_file_description(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    descriptions = {'.md': 'Markdown doc.', '.json': 'JSON data.', '.js': 'JS code.', '.ts': 'TS code.', '.jsx': 'React JS.', '.tsx': 'React TS.', '.py': 'Python.', '.css': 'Styles.', '.html': 'HTML.', '.sh': 'Shell.', '.yaml': 'YAML.', '.sql': 'SQL.'}
    desc = descriptions.get(ext, 'Text file.')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith('# '): desc = f"Doc: {first_line[2:]}"
            elif first_line.startswith('//') or first_line.startswith('/*'): desc = f"Code: {first_line.replace('//', '').replace('/*', '').strip()}"
    except: pass
    return desc

def generate_map(root_dir):
    files_list = []
    gitignore_patterns = load_gitignore_patterns(root_dir)
    exclude_dirs = {'node_modules', 'vendor', '__pycache__', 'dist', 'build', '.next', '.git'}
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not should_exclude(d, os.path.join(root, d), root_dir, gitignore_patterns, exclude_dirs)]
        for file in files:
            file_path = os.path.join(root, file)
            if should_exclude(file, file_path, root_dir, gitignore_patterns, exclude_dirs): continue
            try:
                stats = os.stat(file_path)
                if stats.st_size > 1024 * 1024 or is_binary(file_path): continue
                files_list.append({
                    "path": os.path.relpath(file_path, root_dir),
                    "size_bytes": stats.st_size,
                    "type": mimetypes.guess_type(file_path)[0] or "text/plain",
                    "description": get_file_description(file_path)
                })
            except: continue

    files_list.sort(key=lambda x: x['path'])
    
    # Primeira geração (em memória) para calcular linhas
    initial_data = {
        "version": "1.3",
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_files": len(files_list),
            "line_guide": {f['path']: 0 for f in files_list}
        },
        "files": files_list
    }
    
    json_str = json.dumps(initial_data, indent=2, ensure_ascii=False)
    lines = json_str.split('\n')
    
    # Mapeamento real de linhas
    line_map = {}
    for i, line in enumerate(lines):
        # Procuramos pela linha que abre o objeto do arquivo: "  {"
        # seguida pela linha que contém o path
        if '"path":' in line:
            # O objeto começa na linha anterior à do path (que é o "{")
            path_value = line.split('"path":')[1].strip().strip('",')
            line_map[path_value] = i # i+1 se quisermos 1-indexed, mas como o split é 0-indexed, i já é a linha correta para visualização
            # Ajuste: A IA vê 1-indexed. O split dá 0-indexed.
            # Se a linha do path é 120, o objeto "{" está na 119.
            line_map[path_value] = i # Aponta diretamente para a linha do path para ser infalível

    # Atualiza com o mapa real
    initial_data["summary"]["line_guide"] = line_map
    
    output_dir = os.path.join(root_dir, '.ai-context')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'workspace-map.json')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(initial_data, f, indent=2, ensure_ascii=False)
    
    return output_path

if __name__ == "__main__":
    path = generate_map(os.getcwd())
    print(f"✅ Workspace map updated with Precise Line Guide: {path}")
