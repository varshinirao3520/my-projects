A Computer Vision-Based Project for Detecting Lavender Balloons using YOLO & HSV Thresholding

📌 Overview
This project is a real-time balloon detection system that uses YOLOv8 and HSV color thresholding to detect and track lavender-colored balloons in video feeds. The project integrates deep learning-based object detection (YOLO) and traditional computer vision techniques (HSV filtering, contour detection) to achieve robust detection in different lighting conditions.

📌 Key Features:
✅ YOLOv8-Based Object Detection – Detects balloons using a trained YOLO model
✅ HSV-Based Balloon Masking – Uses color segmentation to isolate lavender balloons
✅ Live Camera Feed Processing – Detects balloons in real-time using OpenCV
✅ Custom Dataset Training – Fine-tuned YOLO on a custom balloon dataset
✅ Optimized Detection Pipeline – Combines deep learning and classical image processing

🛠️ Technologies Used
Python 3.x
YOLOv8 (Ultralytics)
OpenCV
NumPy
TensorFlow/Keras (for potential model training)
Custom Dataset for Balloon Detection

📌 Features & Functionalities
1️⃣ YOLOv8-Based Balloon Detection
Fine-tuned YOLOv8 model on a custom dataset of lavender balloons
Trained on 50 epochs with 640x640 images
Uses bounding boxes and confidence scores to detect balloons
2️⃣ HSV-Based Color Masking
Extracts lavender balloons based on predefined HSV ranges
Uses Gaussian blur and morphological operations to refine the mask
Removes false detections using contour filtering
3️⃣ Real-Time Processing
Uses a webcam feed to detect balloons live
Displays bounding boxes and detection labels
Allows manual saving of detected frames

📌 How It Works
1️⃣ Capture a frame from the webcam
2️⃣ Apply HSV filtering to isolate lavender-colored regions
3️⃣ Detect balloons using YOLOv8 trained on a custom dataset
4️⃣ Overlay bounding boxes and labels on detected balloons
5️⃣ Display the processed frame in real-time

📌 Installation & Setup
🔹 Prerequisites
Ensure you have the following installed:
Python 3.x
OpenCV
Ultralytics YOLO
NumPy
🔹 Clone the Repository
git clone https://github.com/varshinirao3520/my-projects/new/main/Yolo_Object_Detection.git

🔹 Install Dependencies
pip install ultralytics opencv-python numpy

📌 Running the Project
1️⃣ Train YOLO on Custom Dataset
Modify and run train_yolo.py:
python train_yolo.py
📌 Adjust parameters in dataset.yaml (e.g., image paths, number of classes).

2️⃣ Run YOLO Detection on Live Webcam
Use test_yolo_cam.py to detect balloons in real-time:
python test_yolo_cam.py
📌 Press 'q' to exit detection.

3️⃣ Run HSV-Based Balloon Detection
Use Object_Detection.py for color-based detection:
python Object_Detection.py
📌 Adjust HSV values in hsv_values.py for better accuracy.
