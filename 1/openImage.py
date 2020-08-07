import cv2
from pathlib import Path
from os import path

# Relative path where is located the input image.
rootFolder = Path(path.dirname(path.realpath(__file__)))
filepath = rootFolder / "inputs/lena.jpg"

# Open the image as a color image.
image = cv2.imread(str(filepath))

# Show the input image in a OpenCV window.
cv2.imshow("Image", image)
cv2.waitKey(0)

# When everything done, release the OpenCV window.
cv2.destroyAllWindows()
