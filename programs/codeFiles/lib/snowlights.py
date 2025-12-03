import time
from rpi_ws281x import Color
import random

def run(strip, star_count=15, delay=0.05):
    """Snow lights effect: twinkle random LEDs, keep top star."""
    num_pixels = strip.numPixels()
    for _ in range(50):  # number of iterations
        for i in range(num_pixels - star_count):
            color = Color(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            strip.setPixelColor(i, color)
        # Top star always yellow
        for i in range(num_pixels - star_count, num_pixels):
            strip.setPixelColor(i, Color(255, 255, 0))
        strip.show()
        time.sleep(delay)
