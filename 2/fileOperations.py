from pathlib import Path
import os
import cv2
import json

# Folder of this script
rootFolder = Path(os.path.dirname(os.path.realpath(__file__)))
outFolder = rootFolder / "outputs"
imagesFolder = rootFolder / "inputs"

# Create the outputs folder if it doesn't exist
if not os.path.isdir(outFolder):
    os.mkdir(outFolder)

# List that stores the metadata
imgs_data = []
for fileName in os.listdir(imagesFolder):
    # Full path of the file
    filePath = imagesFolder / fileName

    # Check if file exists
    if os.path.isfile(filePath):
        # Load the image from the file path
        img = cv2.imread(str(filePath))

        if img is None:
            print(f"Can't open file as image {filePath}")
        else:
            print(f"Processing image: {filePath}")
            # Get image size
            img_height, img_width = img.shape[:2]
            # Create meta data
            img_data = {
                "name": fileName,
                "height": img_height,
                "width": img_width
            }
            # Add data to the list
            imgs_data.append(img_data)
    else:
        print(f"Can't open file: {filePath}")


# Save the list
dataFilePath = outFolder / "data.json"
with open(dataFilePath, 'w') as outfile:
    print("Saving to:", dataFilePath)
    json.dump(imgs_data, outfile)
