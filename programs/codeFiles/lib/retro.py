from rpi_ws281x import PixelStrip, Color
import time
import config
import random
# ----------------------------
# LED strip configuration
# ----------------------------

STAR_COUNT = config.STAR_COUNT
STAR_COLOR = config.STAR_COLOR
LED_COUNT = config.PIXEL_COUNT
LED_PIN = 12                # GPIO12 (PWM0)
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = int(config.BRIGHTNESS * 255)
LED_INVERT = False
LED_CHANNEL = 0
DELAY = config.DELAY



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




def color_star(strip):
    start = strip.numPixels() - STAR_COUNT
    for i in range(start, strip.numPixels()):
        strip.setPixelColor(i, STAR_COLOR)


def retro_pattern(strip):
    # GRB COLORS
    RED    = Color(0, 255, 0)
    BLUE   = Color(0, 0, 255)
    ORANGE = Color(80, 255, 0)
    GREEN  = Color(255, 0, 0)
    WHITE  = Color(255, 255, 50)

    pattern = [RED, BLUE, ORANGE, GREEN, WHITE]
    group_size = 1          # 5 LEDs per color block
    num_colors = len(pattern)



    for i in range(strip.numPixels()):
        # i // 5 gives block number
        # modulo cycles through the 5 colors
        color_index = (i // group_size) % num_colors
        strip.setPixelColor(i, pattern[color_index])

    strip.show()


    

# ---- RUN PATTERN ----
retro_pattern(strip)
color_star(strip)
strip.show()


