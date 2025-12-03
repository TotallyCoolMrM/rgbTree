# lib/fade_utils.py
import time
import config

NUM_LEDS = config.PIXEL_COUNT

def all_off(strip):
    """Turn all LEDs off immediately."""
    strip.fill((0, 0, 0))
    strip.show()

def fade_out(strip, steps=20, delay=0.05):
    """Smoothly fade all LEDs to off."""
    if NUM_LEDS == 0:
        return

    # assumes all LEDs currently same color
    r, g, b = strip[0]
    
    for step in range(steps, -1, -1):
        factor = step / steps
        strip.fill((int(r * factor), int(g * factor), int(b * factor)))
        strip.show()
        time.sleep(delay)

    all_off(strip)

def demo(strip, delay=2):
    """Simple demo: pause, then fade out."""
    time.sleep(delay)
    fade_out(strip)
