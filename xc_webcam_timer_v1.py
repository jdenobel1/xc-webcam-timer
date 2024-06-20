import cv2
import numpy as np
import pyautogui
import threading

# Function to capture video from webcam
def capture_video(device_num, window_name):
    cap = cv2.VideoCapture(device_num)
    if not cap.isOpened():
        print(f"Error: Unable to open webcam {device_num}")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Failed to read frame from webcam {device_num}")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow(window_name)

# Function to record screen
def record_screen():
    screen = pyautogui.size()
    codec = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("screen_record.avi", codec, 20.0, screen)

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    output.release()
    cv2.destroyAllWindows()

# Start capturing video from two webcams
thread1 = threading.Thread(target=capture_video, args=(0, "Webcam 1"))
thread2 = threading.Thread(target=capture_video, args=(1, "Webcam 2"))
thread1.start()
thread2.start()

# Start recording screen
record_screen()
