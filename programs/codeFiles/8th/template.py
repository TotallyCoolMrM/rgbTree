# ===== DO NOT TOUCH =====
from tree import strip

# Import tree effects
from lib.rainbowChase import rainbow_chase
from lib.solid import solid
from lib.snowlights import snow
from lib.r_gTwinkle import twinkle
# etc...

# ===== STUDENTS START BELOW =====

# Example 1: Rainbow chase
rainbow_chase(strip, wait=0.02)

# Example 2: Solid red for 2 seconds
# solid(strip, (255, 0, 0), time=2)

# Example 3: Twinkle with 3 colors
# twinkle(strip, [(255,0,0), (0,255,0), (0,0,255)], speed=0.1)
