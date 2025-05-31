import os
import shutil

# Paths for images and labels
IMAGE_PATHS = {
    'train_cancer': 'C:/Yolo/dataset/images/train/cancer',
    'train_non_cancer': 'C:/Yolo/dataset/images/train/non-cancer',
    'val_cancer': 'C:/Yolo/dataset/images/validation/cancer',
    'val_non_cancer': 'C:/Yolo/dataset/images/validation/non-cancer',
    'test_cancer': 'C:/Yolo/dataset/images/test/cancer',
    'test_non_cancer': 'C:/Yolo/dataset/images/test/non-cancer'
}

LABEL_PATHS = {
    'train_cancer': 'C:/Yolo/dataset/labels/train/cancer',
    'train_non_cancer': 'C:/Yolo/dataset/labels/train/non-cancer',
    'val_cancer': 'C:/Yolo/dataset/labels/validation/cancer',
    'val_non_cancer': 'C:/Yolo/dataset/labels/validation/non-cancer',
    'test_cancer': 'C:/Yolo/dataset/labels/test/cancer',
    'test_non_cancer': 'C:/Yolo/dataset/labels/test/non-cancer'
}

# Ensure label folders exist
for path in LABEL_PATHS.values():
    os.makedirs(path, exist_ok=True)

# Move label files based on matching image filename
for key, img_path in IMAGE_PATHS.items():
    label_path = LABEL_PATHS[key]
    for file in os.listdir(img_path):
        # Change file extension to .txt
        label_file = file.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')

        # Find the label file
        src_label = os.path.join('C:/Yolo/dataset/labels/test', label_file)  # Assuming all labels are in 'test' initially
        if os.path.exists(src_label):
            shutil.move(src_label, os.path.join(label_path, label_file))
            print(f" Moved {label_file} → {label_path}")

print("\n Labels moved successfully to correct folders!")
