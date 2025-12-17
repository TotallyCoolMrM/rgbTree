#start of file, add all of your imports here #Uncomment the imports you want 
import time
#from lib.retro import run as retro_run
from lib.rainbowChase import run as rainbow_run
from lib.solid import run as solid 
#from lib.twinkle import run as twinkle
#actual code, stuff that will edit the tree 
def run(strip):
    rainbow_run(strip)
    time.sleep(3)


soild(strip, (50,50,50))
