import time
import random
from rpi_ws281x import Color


# Colors in GRB order
RED    = Color(0, 255, 0)
GREEN  = Color(255, 0, 0)
OFF    = Color(0, 0, 0)
COLORS = [RED, GREEN, OFF]


def run(strip, delay=0.3):
    """
    Run the twinkle effect on the LED strip.

    Args:
        strip (PixelStrip): The rpi_ws281x strip object.
        delay (float): Delay between updates.
    """
    try:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, random.choice(COLORS))

        strip.show()
        time.sleep(delay)

    except KeyboardInterrupt:
        clear(strip)


def clear(strip):
    """Turn off all pixels."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, OFF)
    strip.show()
