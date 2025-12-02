from rpi_ws281x import PixelStrip, Color

def apply_star(strip):
    TOTAL_LEDS = strip.numPixels()
    for i in range(TOTAL_LEDS - STAR_COUNT, TOTAL_LEDS):
        strip.setPixelColor(i, Color(*STAR_COLOR))
    strip.show()
