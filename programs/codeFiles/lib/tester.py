import time
import board
import neopixel
import config

LED_PIN = board.D12         # GPIO12
LED_COUNT = config.PIXEL_COUNT
BRIGHTNESS = config.BRIGHTNESS

pixels = neopixel.NeoPixel(
    LED_PIN,
    LED_COUNT,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRB
)

def solid(color, duration=3):
    pixels.fill(color)
    pixels.show()
    time.sleep(duration)

while True: 
    print("WHITE")
    solid((255, 255, 255))

    print("RED")
    solid((255, 0, 0))

    print("GREEN")
    solid((0, 255, 0))

    print("BLUE")
    solid((0, 0, 255))

