import time
from rpi_ws281x import PixelStrip, Color
import config
# --------------------------
# STRIP CONFIG
# --------------------------
LED_COUNT = config.PIXEL_COUNT       # set your number
LED_PIN = 12          # GPIO12 works GREAT
BRIGHTNESS = 128       # 0–255

strip = PixelStrip(
    LED_COUNT, LED_PIN,
    brightness=BRIGHTNESS, 
)
strip.begin()

# --------------------------
# COLOR WHEEL HELPER
# --------------------------
def wheel(pos):
    """Input 0–255 → RGB color."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

# --------------------------
# RAINBOW CHASE EFFECT
# --------------------------
def rainbow_chase(wait=0.02):
    while True:
        for shift in range(256):       # 256-step rainbow
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i + shift) % 256))
            strip.show()
            time.sleep(wait)

# --------------------------
# START THE EFFECT
# --------------------------
if __name__ == "__main__":
    rainbow_chase(0.02)
