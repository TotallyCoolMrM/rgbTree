from lib.retro import run as retro_run
from lib.rainbowChase import run as rainbow_run
from lib.off import all_off as off


def run(strip):
    retro_run(strip)
    rainbow_run(strip)
    off(strip)