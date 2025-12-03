import os
import random
import time
from tree import strip

# Root directory where student scripts live
ROOT_DIR = 'rgpTree/programs/codeFiles'

# Scripts to ignore
IGNORE = {'main.py', 'tree.py', 'config.py'}

# Collect student scripts (Python files that are not ignored)
student_files = [
    f[:-3] for f in os.listdir(ROOT_DIR)
    if f.endswith('.py') and f not in IGNORE
]

if not student_files:
    print(f"No student scripts found in {ROOT_DIR}.")
    exit(1)

print(f"Found student scripts: {student_files}")

while True:
    random.shuffle(student_files)

    for student_name in student_files:
        print(f"Running {student_name}...")
        # Dynamically import the student module
        module_path = f"tree.programs.codeFiles.{student_name}"
        student_module = __import__(module_path, fromlist=['run'])

        # Call the run function from the student script, passing the shared strip
        try:
            student_module.run(strip)
        except Exception as e:
            print(f"Error running {student_name}: {e}")

        # tiny buffer between students
        time.sleep(0.2)
