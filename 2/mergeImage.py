from pathlib import Path
from os import path
import cv2
import numpy as np

# Get the input filename
rootFolder = Path(path.dirname(path.realpath(__file__)))
inputsFolder = rootFolder / "inputs/"
outputsFolder = rootFolder / "out"

img_1 = cv2.imread(str(inputsFolder / "lena.jpg"))
img_2 = cv2.imread(str(inputsFolder / "maddog.jpg"))
# Get dimensions
img_1_height, img_1_width = img_1.shape[:2]
img_2_height, img_2_width = img_2.shape[:2]

# Stack images vertically
# Images have to have the same width in order to be vertically stacked
bigger_width = max(img_1_width, img_2_width)
# Resize both of the images
resized_1 = cv2.resize(img_1, (bigger_width, img_1_height))
resized_2 = cv2.resize(img_2, (bigger_width, img_2_height))

vertical_imgs = np.vstack((resized_1, resized_2))
cv2.imshow("Vertical Stack", vertical_imgs)

# Stack images horizontally
# Images have to have the same height in order to be horizontally stacked
bigger_height = max(img_1_height, img_2_height)
# Resize both of the images
resized_1 = cv2.resize(img_1, (img_1_width, bigger_height))
resized_2 = cv2.resize(img_2, (img_2_width, bigger_height))

horizontal_imgs = np.hstack((resized_1, resized_2))
cv2.imshow("Horizontal Stack", horizontal_imgs)

# End program
cv2.waitKey(0)
cv2.destroyAllWindows()
