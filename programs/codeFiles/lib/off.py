# lib/fade_utils.py

import time
from rpi_ws281x import Color
from codeFiles import config   # ← correct relative import

NUM_LEDS = config.PIXEL_COUNT


def all_off(strip):
    """Turn all LEDs off immediately."""
    for i in range(NUM_LEDS):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


def fade_out(strip, steps=20, delay=0.05):
    """
    Smoothly fade all LEDs to off.
    Assumes LEDs are currently set to (roughly) the same color.
    """

    if NUM_LEDS == 0:
        return

    # rpi_ws281x stores GRB packed in 32 bits
    c = strip.getPixelColor(0)
    g = (c >> 16) & 0xFF
    r = (c >> 8)  & 0xFF
    b = c & 0xFF

    for step in range(steps, -1, -1):
        factor = step / steps
        new_r = int(r * factor)
        new_g = int(g * factor)
        new_b = int(b * factor)

        color = Color(new_r, new_g, new_b)

        for i in range(NUM_LEDS):
            strip.setPixelColor(i, color)

        strip.show()
        time.sleep(delay)

    all_off(strip)


def demo(strip, delay=2):
    """Pause, then fade out."""
    time.sleep(delay)
    fade_out(strip)
