# hardware_tester.py
# Full hardware test for the RGB tree — independent of student code

import time
from rpi_ws281x import PixelStrip, Color

# ===============================
# STRIP CONFIG
# ===============================
LED_COUNT = 300          # number of LEDs
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 80      # lower to reduce flicker
LED_INVERT = False
LED_CHANNEL = 0

# create standalone strip
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

# ===============================
# HELPER FUNCTIONS
# ===============================
def all_off():
    """Turn all LEDs off immediately."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()

def solid(color, wait=1):
    """Fill entire strip with a single color."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait)

def chase(wait=0.02):
    """Single pixel chase around strip."""
    off = Color(0,0,0)
    on  = Color(255,255,255)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, on)
        if i > 0:
            strip.setPixelColor(i-1, off)
        strip.show()
        time.sleep(wait)
    strip.setPixelColor(strip.numPixels()-1, off)
    strip.show()

def wheel(pos):
    """Generate rainbow color from 0-255."""
    if pos < 85:
        return Color(pos*3, 255 - pos*3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos*3, 0, pos*3)
    else:
        pos -= 170
        return Color(0, pos*3, 255 - pos*3)

def rainbow(wait=0.01):
    """Full rainbow wheel test."""
    for j in range(256):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait)

# ===============================
# RUN FULL HARDWARE TEST
# ===============================
if __name__ == "__main__":
    print("Running hardware test…")

    print("Solid red")
    solid(Color(0,255,0))

    print("Solid green")
    solid(Color(255,0,0))

    print("Solid blue")
    solid(Color(0,0,255))

    print("White chase")
    chase()

    print("Rainbow test")
    rainbow()

    print("Turning off LEDs")
    all_off()
    print("Done.")

    # OPTIONAL: infinite teal loop for testing
    while True:
     solid(Color(0,128,128), wait=0)
