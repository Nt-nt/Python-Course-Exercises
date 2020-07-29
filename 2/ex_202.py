from pathlib import Path
import os
import cv2
import json

# Folder of this script
rootFolder = Path(os.path.dirname(os.path.realpath(__file__)))
outFolder = rootFolder / "out"
imagesFolder = rootFolder / "inputs"
dataFilePath = outFolder / "metadata.json"

# Create the outputs folder if it doesn't exist
if not os.path.isdir(outFolder):
    os.mkdir(outFolder)

# List that stores the metadata
imgs_data = []

################################################
# Your code here

# Save the metadata about the images in the inputs folder
# The metadata should contain:
# - The size of the image
# - The absolute path of the image
# - Number of color channels (Hint: use 'img.shape')
################################################
