from pathlib import Path
from os import path
import cv2
import json
import numpy as np

# Folders associated with this script
rootFolder = Path(path.dirname(path.realpath(__file__)))
outFolder = rootFolder / "outputs"
inFolder = rootFolder / "inputs"
tilesFolder = rootFolder / "../common/tiles"
dataFilePath = outFolder / "data.json"

# You have to have a  file named data.json inside the outputs folder
dataJSON = json.loads(open(dataFilePath.resolve()).read())

################################################
# Your code here

# Display a Pokemon tile and its average color side by side.
################################################
