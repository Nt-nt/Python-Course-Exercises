import cv2
from pathlib import Path
import os
import numpy as np

# Create a capture video object.
# Try replacing 1 with 0 if it doesn't work
capture = cv2.VideoCapture(1)

# Define the video resolution.
capture.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create an OpenCV window.
cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)

# This will run while there is a new frame in the video file or
# while the user do not press the "q" (quit) keyboard button.
while True:
    ################################################
    # Make a 3x3 grid of the webcam video such that all the grid tiles display the video

    # Your code here
    ################################################
    pass

# When everything done, release the capture object.
capture.release()
cv2.destroyAllWindows()
