import time
import random
from rpi_ws281x import Color


def run(strip, star_count=15, delay=0.05):
    """Run exactly ONE snow-twinkle update."""
    num_pixels = strip.numPixels()

    # Random twinkles for everything except star area
    for i in range(num_pixels - star_count):
        strip.setPixelColor(
            i,
            Color(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        )

    # Top star section (always yellow)
    for i in range(num_pixels - star_count, num_pixels):
        strip.setPixelColor(i, Color(255, 255, 0))

    strip.show()
    time.sleep(delay)
