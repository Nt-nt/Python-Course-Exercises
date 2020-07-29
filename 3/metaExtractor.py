import cv2
import os
import json
from pathlib import Path

# Get the input filename
rootFolder = Path(os.path.dirname(os.path.realpath(__file__)))
outFolder = rootFolder / "out"
tilesFolder = rootFolder / "tiles/"
dataFilePath = outFolder / "data.json"

if not os.path.isdir(rootFolder / outFolder):
    os.mkdir(outFolder)


def getAverageColor(img):
    return [img[:, :, i].mean() for i in range(img.shape[-1])]


def processImages():
    data = []

    for imgName in os.listdir(tilesFolder):
        img_path = tilesFolder / imgName
        if os.path.isfile(img_path):
            # Loads an image from a file passed as argument.
            img = cv2.imread(str(img_path))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            if img is None:
                print("Can't open", img_path)
                quit()
            print("Processing Image:", imgName)
            data_dict = {}
            data_dict["name"] = imgName
            data_dict["average_color"] = getAverageColor(img)
            data.append(data_dict)
        else:
            print("Not a file:", img_path)
    with open(dataFilePath, 'w') as outfile:
        print("Saving to:", dataFilePath)
        json.dump(data, outfile)
        print("Done")


if os.path.isfile(dataFilePath):
    print("File already exists, overwrite existing file? y/n")
    ans = input()
    if ans == 'y':
        processImages()
    else:
        print("Quitting.")
else:
    processImages()
