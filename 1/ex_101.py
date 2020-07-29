import cv2
from pathlib import Path
import os

# Create a capture video object.
# Try replacing 1 with 0 if it doesn't work
capture = cv2.VideoCapture(1)

# Define the video resolution.
capture.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Setup video recorder
fps = round(capture.get(cv2.CAP_PROP_FPS))
w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
outputFile = str(Path(os.path.dirname(
    os.path.realpath(__file__))) / "outputs/grayscale.mov")
record = cv2.VideoWriter(outputFile, fourcc, fps, (w, h), False)

# Create an OpenCV window.
cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)

# This will run while there is a new frame in the video file or
# while the user do not press the "q" (quit) keyboard button.
while True:
    ################################################
    # The webcam video should be displayed in grayscale.
    # The program should quit when the user hits “q”.
    # Record the video as outputs/grayscale.mov

    # Your code here
    ################################################
    pass

# When everything done, release the capture object.
record.release()
capture.release()
cv2.destroyAllWindows()
