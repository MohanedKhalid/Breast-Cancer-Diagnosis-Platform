import os

# Base path
BASE_PATH = 'C:/Yolo/dataset'

# Define folders
folders = [
    'images/train/cancer',
    'images/train/non-cancer',
    'images/validation/cancer',
    'images/validation/non-cancer',
    'images/test/cancer',
    'images/test/non-cancer',
    'labels/train',
    'labels/validation',
    'labels/test'
]

# Create folders
for folder in folders:
    os.makedirs(os.path.join(BASE_PATH, folder), exist_ok=True)

print("\n Folder structure created!")
