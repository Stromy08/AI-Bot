import time
from pynput.mouse import Controller

# Create a mouse controller
mouse = Controller()

# Open the file and read the data
with open('keysrecord.txt', 'r') as f:
   lines = f.readlines()

# Iterate over the lines
for line in lines:
   # Extract the x and y coordinates
   x, y = map(int, line.split('Pointer moved to ')[1].strip().strip('()').split(', '))
   
   # Move the mouse to the recorded position
   mouse.position = (x, y)
   
   # Wait for a short period of time
   time.sleep(0.1)
   




   