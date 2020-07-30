import cv2
import os
import json
from pathlib import Path

# Get the input filename
rootFolder = Path(os.path.dirname(os.path.realpath(__file__)))
outFolder = rootFolder / "out"
tilesFolder = rootFolder / "../common/tiles"
dataFilePath = outFolder / "data.json"

# Create an output folder if it doesn't already exist
if not os.path.isdir(outFolder):
    os.mkdir(outFolder)


# Calculate and return the average color for the given image
def getAverageColor(img):
    ################################################
    # Your code here
    ################################################
    pass


# Create a list of metadata objects (see handout) and save it as a JSON file
def generateMetadata():
    # Iterate thorugh the tile images
    for imgName in os.listdir(tilesFolder):
        img_path = tilesFolder / imgName
        print(img_path.resolve())

        ################################################
        # Your code here
        ################################################


# Check if the output file exists
if os.path.isfile(dataFilePath):
    print("File already exists, overwrite existing file? y/n")
    ans = input()
    # Overwrite the file if the user inputs 'y'
    if ans == "y" or ans == "Y":
        generateMetadata()
    else:
        print("Quitting.")
else:
    generateMetadata()
