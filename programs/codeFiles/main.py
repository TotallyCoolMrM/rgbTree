import os
import random
import time
import importlib.util
from tree import strip

ROOT_DIR = 'rgbTree/programs/codeFiles/8th'

IGNORE_FILES = {'main.py', 'tree.py', 'config.py','hwtest.py','8th/Template.py'}
IGNORE_DIRS = {'lib'}   
student_files = []

for root, dirs, files in os.walk(ROOT_DIR):

    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

    for f in files:
        if f.endswith('.py') and f not in IGNORE_FILES:
            full_path = os.path.join(root, f)
            student_files.append(full_path)

if not student_files:
    print(f"No student scripts found in {ROOT_DIR}.")
    exit(1)

print("Found student scripts:")
for f in student_files:
    print(" -", f)

def load_module(full_path):
    """Dynamically load a Python file by path."""
    module_name = os.path.splitext(os.path.basename(full_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

while True:
    random.shuffle(student_files)

    for script_path in student_files:
        student_name = os.path.basename(script_path)
        print(f"Running {student_name}...")

        try:
            module = load_module(script_path)
            module.run(strip)
        except Exception as e:
            print(f"Error running {student_name}: {e}")

        time.sleep(0.2)
