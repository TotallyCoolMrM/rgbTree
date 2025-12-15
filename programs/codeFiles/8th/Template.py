#start of file, add all of your imports here #Uncomment the imports you want 
import time
#from lib.retro import run as retro_run
#lib.rainbowChase import run as rainbow_run
from lib.solid import run as solid 
#from lib.twinkle import run as twinkle
#actual code, stuff that will edit the tree 
def run(strip):  
    solid(strip, (0,0,255))
    time.sleep(3)