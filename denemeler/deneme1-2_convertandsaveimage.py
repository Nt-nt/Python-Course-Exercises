import cv2
from os import path
from pathlib import Path

# Bu dosyanın içinde bulunduğu denemeler klasörü
rootFolder = Path(path.dirname(path.realpath(__file__)))

# relative path where is located the input image.
image_path = str(rootFolder / "lenam.jpg")

# Open the image as a grayscale image.
image = cv2.imread(image_path, cv2.IMREAD_ANYDEPTH)

# Show the input image in a OpenCV window.
cv2.imshow("Image", image)
cv2.waitKey(0)

# Save the converted image.
cv2.imwrite(str(rootFolder / "denemeler_cıktı/lenam_grayscale.jpg"), image)

# When everything done, release the OpenCV window.
cv2.destroyAllWindows()
