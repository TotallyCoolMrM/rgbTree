from lib.retro import run as retro_run
from lib.rainbowChase import run as rainbow_run

def run(strip):
    retro_run(strip)
    rainbow_run(strip)
    apply_star(strip)  # restores the top star