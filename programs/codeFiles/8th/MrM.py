import time
import tree
from lib.retro import run as retro_run
from lib.rainbowChase import run as rainbow_run
from lib.snowlights import run as snowlights
from lib.solid import run as solid 
from lib.twinkle import run as twinkle 

def twinkle_timer (strip, seconds=5, delay=.4):
        end = time.time() + seconds
        while time.time() < end:
             twinkle(strip, delay=delay)


def run(strip):
    rainbow_run(strip)
    time.sleep(3)
    retro_run(strip)
    time.sleep(6)
    twinkle(strip, 1)
    twinkle_timer(strip, seconds=5)
    solid(strip, (0,0,255))
    time.sleep(5)
    tree.apply_star(strip)