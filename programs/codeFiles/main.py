import os
import sys
import random
import time
import importlib.util
from tree import strip
import dashboard

IGNORE_FILES = {'main.py', 'dashboard.py', 'tree.py', 'config.py', 'hwtest.py', '8th/Template.py'}
IGNORE_DIRS = {'lib'}
student_files = []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        diffDir = sys.argv[1]
    else:
        diffDir = ""

    ROOT_DIR = os.path.join('rgbTree/programs/codeFiles', diffDir)

# Discover student scripts
for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

    for f in files:
        if f.endswith('.py') and f not in IGNORE_FILES:
            student_files.append(os.path.join(root, f))

if not student_files:
    print(f"No student scripts found in {ROOT_DIR}.")
    exit(1)

def load_module(full_path):
    module_name = os.path.splitext(os.path.basename(full_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

last_run = None

while True:
    random.shuffle(student_files)

    for script_path in student_files:
        student_name = os.path.basename(script_path)
        started_at = time.time()
        error = None

        try:
            module = load_module(script_path)
        except Exception as e:
            error = f"Import failed: {e}"
            dashboard.draw(
                current=student_name,
                last=last_run,
                total=len(student_files),
                error=error,
                started_at=started_at
            )
            time.sleep(2)
            continue

        try:
            dashboard.draw(
                current=student_name,
                last=last_run,
                total=len(student_files),
                started_at=started_at
            )

            module.run(strip)

        except Exception as e:
            error = f"Runtime error: {e}"

        dashboard.draw(
            current=student_name,
            last=last_run,
            total=len(student_files),
            error=error,
            started_at=started_at
        )

        last_run = student_name
        time.sleep(0.2)
