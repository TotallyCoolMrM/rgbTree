# PROPERTY OF ST. MARY'S ACADEMY | GLENS FALLS NY, 12809. CREATED BY TIMMY MCINERNEY

# RGB Tree Classroom Project

This project allows students to control an RGB LED tree using Python on a Raspberry Pi. Effects are modular, safe, and reusable. The setup uses a single shared LED strip object and allows students to create effects without
touching hardware-level code.

---

## Folder Structure

```
rgbTree/
└── programs/
    └── codeFiles/
        ├── main.py            # Main runner for student scripts
        ├── tree.py            # Shared PixelStrip object and star helper
        ├── config.py          # Configuration constants
        ├── lib/               # Library of prebuilt effects
        │   ├── retro.py
        │   ├── rainbowChase.py
        │   ├── solid.py
        │   ├── snowlights.py
        │   └── ...
        └── student_scripts/ # OR GRADES


---

## Running the Project

Use **sudo** to give hardware access while keeping the virtual environment:

```bash
sudo ~/venv/bin/python3 rgbTree/programs/codeFiles/main.py
```

* This runs all student scripts randomly (if `main.py` is configured that way).
* The shared strip is in `tree.py`. All effects and student scripts use this single strip.
* The top LEDs are automatically kept as a star using `apply_star(strip)`.

---

## Writing Student Scripts

Each student script should follow this template:

```python
# ===== DO NOT TOUCH =====
from tree import strip, apply_star
from lib.retro import run as retro_run
from lib.rainbowChase import run as rainbow_run

# ===== STUDENT CODE STARTS HERE =====

def run(strip):
    retro_run(strip)
    rainbow_run(strip)
    apply_star(strip)  # Keeps top LEDs as the star
```

* **All effects must use `strip` passed in as a parameter**.
* Students can call any prebuilt effect from `/lib` or combine multiple effects.
* Do **not** create a new `PixelStrip` in student scripts.

---

## Creating New Effects

To add a new effect:

1. Create a `.py` file in `/lib`.
2. Define a `run(strip, ...)` function.
3. Import it in student scripts as:

```python
from lib.new_effect import run as new_effect_run
new_effect_run(strip)
```

* Always call `apply_star(strip)` after your effect to keep the top LEDs consistent.

---

## Tips

* Avoid running scripts without `sudo` — you’ll get `mmap() failed` errors.
* Virtual environments keep dependencies separate and clean.
* Students can experiment safely without affecting hardware-level code.

---

This setup is classroom-friendly, modular, and ensures all scripts share the same LED strip while preserving the star LEDs at the top.
