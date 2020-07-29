import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from os import path

# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())

rootFolder = Path(path.dirname(path.realpath(__file__)))

# Create the Matplotlib window.
fig = plt.figure()

# Get the input filename
filename = str(rootFolder /
               "inputs/lena.jpg") if args["image"] is None else args["image"]

# BGR image
image = cv2.imread(filename)
img_height, img_width = image.shape[:2]

# Convert images from BGR
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split the image into its channels
channel_r, channel_g, channel_b = cv2.split(image_rgb)

# Create an array of 0s
zeros = np.array(np.zeros((img_height, img_width)), dtype=np.uint8)

# Channels contain only the associated color and black pixels
r_channel = cv2.merge([channel_r, zeros, zeros])
g_channel = cv2.merge([zeros, channel_g, zeros])
b_channel = cv2.merge([zeros, zeros, channel_b])

plt.imshow(b_channel)

# Show the final image.
plt.show()
