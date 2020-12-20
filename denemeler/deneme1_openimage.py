import cv2
from pathlib import Path
from os import path

rootFolder = Path(path.dirname(path.realpath(__file__)))
filepath = rootFolder / "lenam.jpg"

image = cv2.imread(str(filepath))

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
