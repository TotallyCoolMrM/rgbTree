from rpi_ws281x import PixelStrip, Color
import time
import config
import random
# ----------------------------
# LED strip configuration
# ----------------------------
LED_COUNT = config.PIXEL_COUNT       # Number of LED pixels.
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = int(config.BRIGHTNESS * 255)
LED_INVERT = False
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                   LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# ----------------------------
# Zones (index ranges)
# ----------------------------
ZONES = {
    "star":   (LED_COUNT - config.STAR_COUNT, LED_COUNT ),  # star area
    "top":    (2 * (LED_COUNT // 3), LED_COUNT - config.STAR_COUNT - 1),      # top third
    "middle": (LED_COUNT // 3, 2 * (LED_COUNT // 3) - 1),  # middle third
    "bottom": (0, LED_COUNT // 3 - 1),                      # bottom third
    "all":    (0, LED_COUNT - config.STAR_COUNT )            # entire strip except star
}



# GRB color order
COLORS = {
    "red":    Color(0, 255, 0),
    "orange": Color(80, 255, 0),
    "yellow": Color(255, 255, 0),
    "green":  Color(255, 0, 0),
    "blue":   Color(0, 0, 255),
    "indigo": Color(0, 40, 120),
    "violet": Color(120, 0, 120),
    "white":  Color(255, 255, 255),
    "pink":   Color(20,255,147),
    "off":    Color(0, 0, 0),
    "random": Color(random.randint(0,2) * (random.randint(1,10)), random.randint(0,2) * (random.randint(1,10)), random.randint(0,2) * (random.randint(1,10)))
}

def set_zone(zone_name, color_obj, brightness=None):
    start, end = ZONES[zone_name]
    if brightness is not None:
        strip.setBrightness(brightness)
    for i in reversed(range(start, end)):
        strip.setPixelColor(i, color_obj)
    strip.show()


print("Commands:")
print("  <zone> <color> [brightness]")
print("Zones:", ", ".join(ZONES.keys()))
print("Colors:", ", ".join(COLORS.keys()))
print("Examples:")
print("  top yellow 200")
print("  middle green 50")
print("  bottom red")
print("  top off")
print("Press Ctrl+C to exit.\n")

try:
    while True:
        cmd = input("> ").strip().lower()
        parts = cmd.split()
        if len(parts) < 2:
            print("Usage: <zone> <color> [brightness]")
            continue

        zone, color_name = parts[0], parts[1]

        if zone not in ZONES:
            print("Unknown zone:", zone)
            continue

        if color_name not in COLORS:
            print("Unknown color:", color_name)
            continue

        brightness = None
        if len(parts) == 3 and parts[2].isdigit():
            brightness = max(0, min(255, int(parts[2])))

        set_zone(zone, COLORS[color_name], brightness)
        print(f"Set {zone} to {color_name}" + (f" @ {brightness}" if brightness else ""))

except KeyboardInterrupt:
    print("\nTurning LEDs off...")
    for zone in ZONES:
        set_zone(zone, COLORS["off"])
