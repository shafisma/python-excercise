import time
import os

text = ">>> Moving Text >>>"
for pos in range(50):
    print(" " * pos + text)  # Shift text
    time.sleep(0.02)         # Speed of movement
    os.system('cls' if os.name == 'nt' else 'clear')
