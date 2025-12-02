import time
import random
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 250
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 200
LED_INVERT = False
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                   LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# ----------------------------------------------------
# COLOR ZONES — Top orange → middle yellow → bottom white
# ----------------------------------------------------
TOP_COLOR    = (255, 140, 10)   # deep warm orange
MID_COLOR    = (255, 200, 40)   # warm yellow
BOTTOM_COLOR = (255, 255, 200)  # soft warm white

# how much each LED is allowed to flicker
FLICKER_MIN = -40
FLICKER_MAX = +25


def lerp(a, b, t):
    """Linear interpolate between two values."""
    return a + (b - a) * t


def blend(c1, c2, t):
    """Blend two RGB colors."""
    return (
        int(lerp(c1[0], c2[0], t)),
        int(lerp(c1[1], c2[1], t)),
        int(lerp(c1[2], c2[2], t)),
    )


# ----------------------------------------------------
# PRECOMPUTE the gradient for speed
# ----------------------------------------------------
gradient = []

for i in range(LED_COUNT):
    pos = i / (LED_COUNT - 1)

    if pos < 0.5:
        # top → middle
        t = pos / 0.5
        gradient.append(blend(TOP_COLOR, MID_COLOR, t))
    else:
        # middle → bottom
        t = (pos - 0.5) / 0.5
        gradient.append(blend(MID_COLOR, BOTTOM_COLOR, t))


def flicker(color):
    """Return this pixel's flickered version."""
    g = color[0] + random.randint(FLICKER_MIN, FLICKER_MAX)
    r = color[1] + random.randint(FLICKER_MIN, FLICKER_MAX)
    b = color[2] + random.randint(FLICKER_MIN, FLICKER_MAX)

    # clamp 0–255
    return (
        max(0, min(255, g)),
        max(0, min(255, r)),
        max(0, min(255, b)),
    )


try:
    while True:
        for i in range(LED_COUNT):
            (g, r, b) = flicker(gradient[i])
            strip.setPixelColor(i, Color(g, r, b))

        strip.show()
        time.sleep(random.uniform(0.02, 0.08))

except KeyboardInterrupt:
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()
