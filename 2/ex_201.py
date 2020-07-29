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

image = cv2.imread(filename)

################################################
# Your code here

# Convert images from BGR to HSV
# Split the image into its channels
# Create an array of 0s
# Display the H, S, and V channels
################################################

# Show the final image.
plt.show()
