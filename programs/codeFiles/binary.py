import board
import neopixel
import time
import random
import config

# ----------------------------
# Tree configuration
# ----------------------------
TOTAL_LEDS = config.PIXEL_COUNT

# NeoPixel setup
LED_PIN = board.D18
LED_BRIGHTNESS = config.BRIGHTNESS
strip = neopixel.NeoPixel(LED_PIN, TOTAL_LEDS, brightness=LED_BRIGHTNESS, auto_write=False)

# LED state (0=off, 1=green)
led_state = [0] * TOTAL_LEDS

# ----------------------------
# Helper functions
# ----------------------------
def phys(i):
    """Map logical index to physical reversed index."""
    return TOTAL_LEDS - 1 - i

def update_strip():
    """Send led_state to physical LEDs (with reversed mapping)."""
    for i in range(TOTAL_LEDS):
        idx = phys(i)
        if led_state[i]:
            strip[idx] = (255, 0, 0)   # green
        else:
            strip[idx] = (0, 0, 0)
    strip.show()

# ----------------------------
# Main loop
# ----------------------------
try:
    while True:
        # Shift LEDs down (top -> bottom logically)
        for i in range(TOTAL_LEDS - 1, 0, -1):
            led_state[i] = led_state[i - 1]

        # Random new drop at the logical top row
        led_state[0] = random.choice([0, 1])

        update_strip()
        time.sleep(0.1)

except KeyboardInterrupt:
    for i in range(TOTAL_LEDS):
        strip[i] = (0,0,0)
    strip.show()
    print("LED tree stopped.")
