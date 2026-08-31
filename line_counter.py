# line_counter.py
"""
System utility script to scan all project directories and count lines of Python code.
Ensures project requirement compliance (>50k lines).
"""
import os

def count_lines(directory):
    total_lines = 0
    py_files = 0
    
    print(f"\nScanning directory: {directory}\n" + "-"*40)
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv', '.pytest_cache']]
        
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = len(f.readlines())
                        total_lines += lines
                        py_files += 1
                        rel_path = os.path.relpath(filepath, directory)
                        print(f"  {rel_path:<40} : {lines:>5} lines")
                except Exception as e:
                    print(f"  Could not read {filepath}: {e}")
                    
    print("-"*40)
    print(f"Total Python Files: {py_files}")
    print(f"Total Lines of Python Code: {total_lines}")
    print("-"*40)
    return total_lines, py_files

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    count_lines(current_dir)
