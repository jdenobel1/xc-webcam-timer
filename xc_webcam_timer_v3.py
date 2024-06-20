import cv2
import numpy as np
import pyautogui
import threading
import time
import keyboard  # You may need to install the keyboard module

# Global variables for the stopwatch
start_time = None
running = False
time_str = "00:00:00.00"
recorded_times = []
txt_file_name = "times.txt"
screen_recording_file_name = "screen_record.avi"

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
            with open(txt_file_name, "a") as file:
                file.write(time_str + "\n")
            print(f"Recorded: Time {time_str}")

    cap.release()
    cv2.destroyWindow(window_name)

# Function to record screen
def record_screen():
    global screen_recording_file_name
    screen = pyautogui.size()
    codec = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter(screen_recording_file_name, codec, 20.0, (screen.width, screen.height))

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)

        if keyboard.is_pressed('ctrl+shift+s'):  # Hotkey to stop the screen recording
            print("Stopping screen recording...")
            break

    output.release()
    cv2.destroyAllWindows()

# Function to start the screen recording
def start_screen_recording():
    global screen_recording_file_name
    screen_recording_file_name = input("Enter the name for the screen recording file (with .avi extension): ")
    if not screen_recording_file_name.endswith('.avi'):
        screen_recording_file_name += '.avi'
    
    screen_recording_thread = threading.Thread(target=record_screen)
    screen_recording_thread.start()

# Function to set the text file name
def set_file_names():
    global txt_file_name
    txt_file_name = input("Enter the name for the text file (with .txt extension): ")
    if not txt_file_name.endswith('.txt'):
        txt_file_name += '.txt'

# Start the stopwatch thread
stopwatch_thread = threading.Thread(target=update_stopwatch)
stopwatch_thread.start()

# Set the text file name
set_file_names()

# Start capturing video from two webcams
thread1 = threading.Thread(target=capture_video, args=(0, "Webcam 1"))
thread2 = threading.Thread(target=capture_video, args=(1, "Webcam 2"))
thread1.start()
thread2.start()

# Wait for hotkey sequence to start screen recording
print("Press 'ctrl+shift+r' to start screen recording")
keyboard.wait('ctrl+shift+r')
print("Starting screen recording...")
start_screen_recording()
