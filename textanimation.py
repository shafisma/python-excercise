import time
import os

text = ">>> Moving Text >>>"
for pos in range(50):
    print(" " * pos + text) 
    time.sleep(0.02)
    os.system('cls' if os.name == 'nt' else 'clear')
