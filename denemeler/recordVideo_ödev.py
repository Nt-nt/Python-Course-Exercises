import cv2
from pathlib import Path
from os import path


rootFolder = Path(path.dirname(path.realpath(__file__)))

# relative path where is located the input image.
video_path = str(rootFolder / "örnek_1.mp4")

# Create a capture video object.
# Try replacing 1 with 0 if it doesn't work
capture = cv2.VideoCapture(video_path)

# Define the video resolution.
w= int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h= int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = round(capture.get(cv2.CAP_PROP_FPS))

# Check if the fps variable has a correct value.
fps = fps if fps > 0 else 30

# Create a record video object.
isColor = True
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
outputFile = str(rootFolder / "Video_ödev.mp4")
record = cv2.VideoWriter(outputFile, fourcc, fps, (w, h), isColor)


# Create an OpenCV window.
cv2.namedWindow("Video_ödev", cv2.WINDOW_AUTOSIZE)

# This will run while there is a new frame in the video file or
# while the user do not press the "q" (quit) keyboard button.
while True:
    # Capture the frame
    retval, frame = capture.read()

    # Check if there is a valid frame.
    if not retval:
        break
    
    # Convert the input image from BGR to Grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame.
    cv2.imshow("Video_ödev", grayscale)

    record.write(grayscale)

    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

# When everything done, release the capture object.
record.release()
capture.release()
cv2.destroyAllWindows()

