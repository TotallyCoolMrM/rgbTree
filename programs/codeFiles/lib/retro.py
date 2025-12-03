from rpi_ws281x import Color

def run(strip):
    """Retro repeating-color stripe pattern."""
    RED    = Color(0, 255, 0)
    BLUE   = Color(0, 0, 255)
    ORANGE = Color(80, 255, 0)
    GREEN  = Color(255, 0, 0)
    WHITE  = Color(255, 255, 50)

    pattern = [RED, BLUE, ORANGE, GREEN, WHITE]
    group_size = 1

    for i in range(strip.numPixels()):
        color_index = (i // group_size) % len(pattern)
        strip.setPixelColor(i, pattern[color_index])

    strip.show()
