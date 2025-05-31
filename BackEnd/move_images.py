import os
import shutil
import random

# Source paths (Updated to Augmented Dataset)
SOURCE_CANCER = 'C:/Yolo/Breast Cancer Dataset/Augmented Dataset/Cancer'
SOURCE_NON_CANCER = 'C:/Yolo/Breast Cancer Dataset/Augmented Dataset/Non-Cancer'

# Destination paths
DEST = {
    'train': {
        'cancer': 'C:/Yolo/dataset/images/train/cancer',
        'non-cancer': 'C:/Yolo/dataset/images/train/non-cancer'
    },
    'validation': {
        'cancer': 'C:/Yolo/dataset/images/validation/cancer',
        'non-cancer': 'C:/Yolo/dataset/images/validation/non-cancer'
    },
    'test': {
        'cancer': 'C:/Yolo/dataset/images/test/cancer',
        'non-cancer': 'C:/Yolo/dataset/images/test/non-cancer'
    }
}

# Split ratio
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

# Function to move files
def split_and_move(source, dest):
    files = [f for f in os.listdir(source) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(files)

    train_size = int(len(files) * TRAIN_RATIO)
    val_size = int(len(files) * VAL_RATIO)

    for i, file in enumerate(files):
        src_file = os.path.join(source, file)

        if i < train_size:
            target = dest['train']
        elif i < train_size + val_size:
            target = dest['validation']
        else:
            target = dest['test']

        shutil.move(src_file, target)
        print(f" Moved {file} → {target}")

# Move cancer images
split_and_move(SOURCE_CANCER, {
    'train': DEST['train']['cancer'],
    'validation': DEST['validation']['cancer'],
    'test': DEST['test']['cancer']
})

# Move non-cancer images
split_and_move(SOURCE_NON_CANCER, {
    'train': DEST['train']['non-cancer'],
    'validation': DEST['validation']['non-cancer'],
    'test': DEST['test']['non-cancer']
})

print("\n Augmented dataset moved successfully!")
