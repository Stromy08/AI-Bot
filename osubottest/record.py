import pyautogui
import cv2
import time
import numpy as np

def record_gameplay(duration, output_video_path, output_input_path):
    # OpenCV video writer setup
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec as needed
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 60.0, screen_size)

    # Input recording setup
    inputs = []

    start_time = time.time()

    while time.time() - start_time < duration:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Write frame to video
        video_writer.write(frame)

        # Record mouse and keyboard inputs
        mouse_pos = pyautogui.position()
        key_state = pyautogui.KEYBOARD_KEYS  # Replace with actual keyboard input tracking

        inputs.append({
            'frame_number': int((time.time() - start_time) * 60),  # Assuming 60 fps
            'mouse_pos': mouse_pos,
            'key_state': key_state
        })

        time.sleep(1 / 60)  # Assuming 60 fps, adjust as needed

    # Release video writer
    video_writer.release()

    # Save inputs to a text file
    with open(output_input_path, 'w') as file:
        for entry in inputs:
            file.write(f"Frame {entry['frame_number']}:\n")
            file.write(f"Mouse Position: {entry['mouse_pos']}\n")
            file.write(f"Key State: {entry['key_state']}\n")
            file.write("\n")

    return output_video_path, output_input_path
