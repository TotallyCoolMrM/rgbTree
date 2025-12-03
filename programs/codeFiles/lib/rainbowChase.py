import time
from rpi_ws281x import Color

def run(strip, wait=0.02):
    """Rainbow chase effect."""
    def wheel(pos):
        if pos < 85:
            return Color(pos*3, 255-pos*3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255-pos*3, 0, pos*3)
        else:
            pos -= 170
            return Color(0, pos*3, 255-pos*3)

    for shift in range(256):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+shift)%256))
        strip.show()
        time.sleep(wait)
