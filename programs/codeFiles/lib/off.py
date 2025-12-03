# lib/fade_utils.py

import time
from tree import strip     # <-- use shared strip!
import config

NUM_LEDS = config.PIXEL_COUNT

# ----- HELPER FUNCTIONS -----
def all_off():
    """Turn all LEDs off immediately."""
    strip.fill((0, 0, 0))
    strip.show()

def fade_out(steps=20, delay=0.05):
    """Smoothly fade all LEDs to off."""
    if NUM_LEDS == 0:
        return

    r, g, b = strip[0]  # assumes uniform color
    for step in range(steps, -1, -1):
        factor = step / steps
        strip.fill((int(r*factor), int(g*factor), int(b*factor)))
        strip.show()
        time.sleep(delay)

    all_off()

def demo(delay=2):
    """Simple demo: pause, then fade out."""
    time.sleep(delay)
    fade_out()
