import time
import board
import neopixel
import config

# ----- CONFIG -----
LED_PIN = board.D18
NUM_LEDS = config.PIXEL_COUNT
BRIGHTNESS = config.BRIGHTNESS

# ----- SETUP -----
strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# ----- HELPER FUNCTIONS -----
def all_off():
    """Turn all LEDs off immediately."""
    strip.fill((0, 0, 0))
    strip.show()

def fade_out(steps=20, delay=0.05):
    """Smoothly fade all LEDs to off."""
    # Get current color of first pixel as reference (assuming uniform color)
    if NUM_LEDS == 0:
        return
    r, g, b = strip[0]
    for step in range(steps, -1, -1):
        factor = step / steps
        strip.fill((int(r*factor), int(g*factor), int(b*factor)))
        strip.show()
        time.sleep(delay)
    all_off()

def demo():
    """Simple demo: turn red on, wait, then fade out."""
   
    time.sleep(2)
    fade_out()

# ----- RUN DEMO -----
if __name__ == "__main__":
    demo()

