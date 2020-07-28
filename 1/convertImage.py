import cv2

# Full path where is located the input image.
filepath = "./inputs/lena.jpg"

# Open the image as a color image.
image_bgr = cv2.imread(filepath, cv2.IMREAD_COLOR)

# Convert the input image from BGR to Grayscale
grayscale = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Show the input image in a OpenCV window.
cv2.imshow("Image", image_rgb)
#cv2.imshow("Grayscale", grayscale)
cv2.waitKey(0)

# When everything done, release the OpenCV window.
cv2.destroyAllWindows()
