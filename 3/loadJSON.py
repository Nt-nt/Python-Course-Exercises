from pathlib import Path
import os
import cv2
import json

# Folder of this script
rootFolder = Path(os.path.dirname(os.path.realpath(__file__)))
outFolder = rootFolder / "outputs"
inFolder = rootFolder / "inputs"
tilesFolder = rootFolder / "../common/tiles"
dataFilePath = inFolder / "imgSizes.json"

# Load the content of the file as a Python list
dataJSON = json.loads(open(dataFilePath.resolve()).read())

# metaData is a Python dictionary
for metaData in dataJSON:
    # Get values from the dictionary
    imgName = metaData['name']
    imgHeight = metaData['height']
    imgWidth = metaData['width']

    print(f"{imgName} has a size of {imgHeight}X{imgWidth}")
