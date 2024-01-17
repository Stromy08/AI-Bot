import pyautogui
import cv2
import numpy as np
import keyboard
from pynput import mouse
import time
import keyboard
import logging



screen_size = (1920, 1080)  # Change this to match your screen resolution
fps = 30
output_filename = input("enter filename: \n")
video_filename = output_filename + ".avi"



fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(video_filename, fourcc, fps, screen_size)

def record_screen():
        # Capture screen content
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    # Convert BGR format (used by OpenCV) to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)



#--- KEY LOGGER ---#
    
# Create a logger
logger = logging.getLogger(__name__)

# Set the level of the logger. This can be DEBUG, INFO, WARNING, ERROR, CRITICAL.
logger.setLevel(logging.DEBUG)
txt_filename = output_filename + ".txt"
# Create a file handler
handler = logging.FileHandler(txt_filename)

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

    #run code from above
    record_screen()

   # Stop recording when the user presses the 'q' key    #--- DOESN'T WORK! ---#
#    if cv2.waitKey(1) == ord("q"):                      #--- DOESN'T WORK! ---#
#        break                                           #--- DOESN'T WORK! ---#

# Release the VideoWriter and close the OpenCV windows
out.release()
cv2.destroyAllWindows()

#sample text for testing
#This is a sample text!