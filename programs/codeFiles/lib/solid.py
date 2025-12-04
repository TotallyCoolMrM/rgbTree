from rpi_ws281x import Color

def run(strip, color=(0, 220, 255)):
    """Fill the whole strip with a solid color."""
    r, g, b = color
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(r, g, b))
    strip.show()
