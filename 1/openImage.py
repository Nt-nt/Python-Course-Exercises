import cv2

# Relative path where is located the input image.
filepath = "./inputs/lena.jpg"

# Open the image as a color image.
image = cv2.imread(filepath)

# Show the input image in a OpenCV window.
cv2.imshow("Image", image)
cv2.waitKey(0)

# When everything done, release the OpenCV window.
cv2.destroyAllWindows()
