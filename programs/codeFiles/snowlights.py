import time
import board
import neopixel
import random
import config


# ----- CONFIG -----
LED_PIN = board.D18
NUM_LEDS = config.PIXEL_COUNT
BRIGHTNESS = config.BRIGHTNESS
DELAY = config.DELAY

# ----- SETUP -----
strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# ----- RANDOM RAINBOW -----
def random_color():
    """Return a random RGB color tuple."""
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

try:
    while True:
        for i in range(NUM_LEDS):
            strip[i] = random_color()
        strip.show()
        time.sleep(DELAY)

except KeyboardInterrupt:
    # pause LEDs when stopping
    strip.show()
    print("Random rainbow stopped.")
