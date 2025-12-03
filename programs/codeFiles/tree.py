from rpi_ws281x import PixelStrip, Color
import config

# ----- STRIP CONFIG -----
LED_COUNT = config.PIXEL_COUNT
LED_PIN = 12
BRIGHTNESS = int(config.BRIGHTNESS * 255)  # ensure it's 0–255
STAR_COUNT = getattr(config, "STAR_COUNT", 15)  # default 15 top LEDs
STAR_COLOR = getattr(config, "STAR_COLOR", Color(255, 255, 0))  # yellow star

# Create the single shared strip
strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    brightness=BRIGHTNESS
)
strip.begin()

# ----- HELPER FUNCTION -----
def apply_star(strip, star_count=STAR_COUNT, star_color=STAR_COLOR):
    """Force the top `star_count` LEDs to a fixed color."""
    for i in range(strip.numPixels() - star_count, strip.numPixels()):
        strip.setPixelColor(i, star_color)
    strip.show()
