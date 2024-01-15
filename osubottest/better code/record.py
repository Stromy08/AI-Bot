import pyautogui
import cv2
import numpy as np




screen_size = (1920, 1080)  # Change this to match your screen resolution
fps = 30
output_filename = input("enter filename: \n") + ".avi"




fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, fourcc, fps, screen_size)

def record_screen():
        # Capture screen content
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    # Convert BGR format (used by OpenCV) to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

def record_inputs():
    print("oky")


while True:

    #run code from above
    record_screen()
    # Stop recording when the user presses the 'q' key  #--- DOESN'T WORK! ---#
    if cv2.waitKey(1) == ord("q"):                      #--- DOESN'T WORK! ---#
        break                                           #--- DOESN'T WORK! ---#

# Release the VideoWriter and close the OpenCV windows
out.release()
cv2.destroyAllWindows()

