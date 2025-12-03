from rpi_ws281x import PixelStrip
import config

LED_COUNT = config.PIXEL_COUNT
LED_PIN = 12
BRIGHTNESS = config.BRIGHTNESS

strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    brightness=BRIGHTNESS
)

strip.begin()

