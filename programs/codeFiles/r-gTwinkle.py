import time
import random
import config
from rpi_ws281x import PixelStrip, Color


# ----- CONFIG -----
LED_COUNT = config.PIXEL_COUNT
LED_PIN = 12                # GPIO12 (PWM0)
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = int(config.BRIGHTNESS * 255)
LED_INVERT = False
LED_CHANNEL = 0
DELAY = config.DELAY
STAR_COLOR = config.STAR_COLOR



# ----- SETUP -----
strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    LED_FREQ_HZ,
    LED_DMA,
    LED_INVERT,
    LED_BRIGHTNESS,
    LED_CHANNEL
)
strip.begin()

# ----- COLORS (GRB order!) -----
RED    = Color(0, 255, 0)
GREEN  = Color(255, 0, 0)
OFF    = Color(0, 0, 0)
colors = [RED, GREEN, OFF]

# ----- TWINKLE LOOP -----
try:
    while True:
        for i in range(strip.numPixels() - config.STAR_COUNT):
            strip.setPixelColor(i, random.choice(colors))

        for i in range(LED_COUNT - config.STAR_COUNT):
            strip.show()
            strip.setPixelColor(STAR_COLOR)
        
        time.sleep(DELAY)

except KeyboardInterrupt:

    strip.show()
    print("Twinkle stopped.")
