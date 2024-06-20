# xc-webcam-timer

Updates of the xc-webcam-timer
Currently stable release is xc-webcam-timer_v4
Will be updating more. Also have found xcscoreboard ( https://github.com/xcscoreboard/xcscoreboard ) -- not my program | but good version 

Stopwatch, Webcam Capture, and Screen Recording Script

This Python script provides functionality for a stopwatch with overlay, captures video from two webcams simultaneously, and records the screen using a hotkey.
Features:

    Stopwatch: Displays elapsed time with a green overlay on webcam feeds.
    Webcam Capture: Displays video from two webcams with a resizable window.
    Screen Recording: Records the screen until a hotkey is pressed to stop.

Requirements:

    Python 3.x
    OpenCV (pip install opencv-python)
    PyAutoGUI (pip install pyautogui)
    Keyboard (pip install keyboard)

How to Use:

    Install Dependencies:

    bash

pip install opencv-python pyautogui keyboard

Run the Script:

bash

python main.py

Using the Script:

    Stopwatch:
        Press Spacebar to start or stop the stopwatch.
        Press Enter to record the current time to a text file (times.txt).
        Press Q to quit the webcam capture.

    Webcam Capture:
        Two webcam windows will open side by side.
        The stopwatch overlay will be displayed on each webcam feed.
        Resize the window to adjust the size of the webcam display.

    Screen Recording:
        Press Ctrl + Shift + R to start recording the screen.
        Press Ctrl + Shift + S to stop recording.

Output Files:

    Text File: times.txt records the times recorded using the Enter key.
    Screen Recording File: Specify the screen recording file name with a .avi extension.


Notes:

    This script captures video from two webcams, displays a stopwatch overlay, and records the screen.
    Make sure to install the required Python packages (opencv-python, pyautogui, keyboard) before running the script.
    Adjust the script as needed for your use case, such as changing file names or hotkeys.

Author:

    Author: Jason deNobel
  
MIT License

Copyright (c) 2024 Jason deNobel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
