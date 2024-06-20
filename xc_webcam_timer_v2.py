import cv2
import numpy as np
import pyautogui
import threading
import time

# Global variables for the stopwatch
start_time = None
running = False
time_str = "00:00:00.00"
recorded_times = []

# Function to update the stopwatch
def update_stopwatch():
    global start_time, running, time_str
    while True:
        if running:
            elapsed_time = time.time() - start_time
            hours, rem = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(rem, 60)
            hundredths = int((seconds - int(seconds)) * 100)
            time_str = "{:02}:{:02}:{:02}.{:02}".format(int(hours), int(minutes), int(seconds), hundredths)
        time.sleep(0.01)

# Function to capture video from webcam
def capture_video(device_num, window_name):
    global time_str
    cap = cv2.VideoCapture(device_num)
    if not cap.isOpened():
        print(f"Error: Unable to open webcam {device_num}")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Failed to read frame from webcam {device_num}")
            break

        # Overlay stopwatch on the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, time_str, (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord(' '):  # Spacebar to start/stop the timer
            global running, start_time
            if running:
                running = False
            else:
                running = True
                start_time = time.time()
        elif key == ord('\r'):  # Enter key to save the time
            recorded_times.append(time_str)
            with open("times.txt", "a") as file:
                file.write(time_str + "\n")

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

# Start the stopwatch thread
stopwatch_thread = threading.Thread(target=update_stopwatch)
stopwatch_thread.start()

# Start capturing video from two webcams
thread1 = threading.Thread(target=capture_video, args=(0, "Webcam 1"))
thread2 = threading.Thread(target=capture_video, args=(1, "Webcam 2"))
thread1.start()
thread2.start()

# Start recording screen
record_screen()
