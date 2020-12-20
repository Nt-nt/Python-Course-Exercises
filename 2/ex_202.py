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

# Fotoğraflar ile ilgili bilgileri bir JSON dosyasına kaydet. Bilgilerde:
# - Fotoğrafın en, boy ve renk derinliği
# - Fotoğrafın uzun dosya konumu olmalı
# Örnek: [{"path": "/home/ken/Documents/Course/Python-Course-Exercises/2/inputs/lena.jpg", "height": 512, "width": 512, "depth": 3}]