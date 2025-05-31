import os

# Paths
DATASET_PATH = 'C:/Yolo/dataset'
IMAGE_PATHS = {
    'train_cancer': os.path.join(DATASET_PATH, 'images/train/cancer'),
    'train_non_cancer': os.path.join(DATASET_PATH, 'images/train/non-cancer'),
    'val_cancer': os.path.join(DATASET_PATH, 'images/validation/cancer'),
    'val_non_cancer': os.path.join(DATASET_PATH, 'images/validation/non-cancer'),
    'test_cancer': os.path.join(DATASET_PATH, 'images/test/cancer'),
    'test_non_cancer': os.path.join(DATASET_PATH, 'images/test/non-cancer')
}

LABEL_PATHS = {
    'train_cancer': os.path.join(DATASET_PATH, 'labels/train/cancer'),
    'train_non_cancer': os.path.join(DATASET_PATH, 'labels/train/non-cancer'),
    'val_cancer': os.path.join(DATASET_PATH, 'labels/validation/cancer'),
    'val_non_cancer': os.path.join(DATASET_PATH, 'labels/validation/non-cancer'),
    'test_cancer': os.path.join(DATASET_PATH, 'labels/test/cancer'),
    'test_non_cancer': os.path.join(DATASET_PATH, 'labels/test/non-cancer')
}

# Class mapping
CLASS_MAP = {
    'cancer': 0,
    'non-cancer': 1
}

#  Ensure label folders exist
for path in LABEL_PATHS.values():
    os.makedirs(path, exist_ok=True)

# Function to create YOLO labels
def create_manual_labels(image_dir, label_dir, class_id):
    created_labels = 0

    if not os.path.exists(image_dir):
        return

    for img_file in os.listdir(image_dir):
        if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Create label file path
            label_file = os.path.join(label_dir, img_file.replace('.jpg', '.txt')
                                                    .replace('.jpeg', '.txt')
                                                    .replace('.png', '.txt'))

            #  Create a basic YOLO bounding box
            x_center, y_center = 0.5, 0.5
            width, height = 0.5, 0.5

            try:
                with open(label_file, 'w') as f:
                    f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
                print(f" Created label for: {img_file} → {label_file}")
                created_labels += 1
            except Exception as e:
                print(f" Error writing file: {e}")

    print(f"\n Total labels created in '{label_dir}': {created_labels}\n")

#  Generate labels for each folder
create_manual_labels(IMAGE_PATHS['train_cancer'], LABEL_PATHS['train_cancer'], CLASS_MAP['cancer'])
create_manual_labels(IMAGE_PATHS['train_non_cancer'], LABEL_PATHS['train_non_cancer'], CLASS_MAP['non-cancer'])
create_manual_labels(IMAGE_PATHS['val_cancer'], LABEL_PATHS['val_cancer'], CLASS_MAP['cancer'])
create_manual_labels(IMAGE_PATHS['val_non_cancer'], LABEL_PATHS['val_non_cancer'], CLASS_MAP['non-cancer'])
create_manual_labels(IMAGE_PATHS['test_cancer'], LABEL_PATHS['test_cancer'], CLASS_MAP['cancer'])
create_manual_labels(IMAGE_PATHS['test_non_cancer'], LABEL_PATHS['test_non_cancer'], CLASS_MAP['non-cancer'])

print("\n YOLO labels generated successfully!")
