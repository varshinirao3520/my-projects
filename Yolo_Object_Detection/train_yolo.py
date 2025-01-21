from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')  # Use 'yolov8n.pt' for the Nano version

# Train the model on the custom dataset
model.train(data='dataset.yaml', epochs=50, imgsz=640)
