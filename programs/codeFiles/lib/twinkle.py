import time
import random

from rpi_ws281x import PixelStrip, Color


# ----- CONFIG -----
LED_COUNT = 200
LED_PIN = 12                # GPIO12 (PWM0)
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = int(.5 * 255)
LED_INVERT = False
LED_CHANNEL = 0
DELAY =.1
STAR_COLOR = (0,0,0)



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
        for i in range(strip.numPixels() - 15):
            strip.setPixelColor(i, random.choice(colors))

        for i in range(200 - 15):
            strip.show()
            strip.setPixelColor(STAR_COLOR)
        
        time.sleep(DELAY)

except KeyboardInterrupt:

    strip.show()
    print("Twinkle stopped.")
