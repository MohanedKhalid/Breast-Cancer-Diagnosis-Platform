from ultralytics import YOLO

#  Load last checkpoint to resume training
model = YOLO('runs/detect/train6/weights/last.pt')

#  Resume training from the last epoch
train_results = model.train(
    data='dataset.yaml',
    epochs=50,         # It will continue from the last epoch automatically
    imgsz=640,         # Keep resolution at 640 for better detection
    batch=16,          # Adjust based on GPU memory
    workers=4,
    patience=10,       # Early stopping if no improvement after 10 epochs
    optimizer='SGD',   # SGD tends to converge better for detection tasks
    resume=True         #  This enables resuming training!
)

#  Save the trained model
model.save('models/yolov8-cancer-detection.pt')

#  Evaluate model on validation set
val_results = model.val()

# Test model on test images
test_results = model.predict(
    'dataset/images/test',
    save=True,
    conf=0.5,           # Minimum confidence threshold
    project='runs/detect',
    name='cancer_test'
)

#  Display results separately
print("\n Training Results:")
print(train_results)

print("\n Validation Results:")
print(val_results)

print("\n Test Results:")
print(test_results)
