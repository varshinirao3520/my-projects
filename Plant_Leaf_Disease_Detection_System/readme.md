A Deep Learning-Based System for Identifying Plant Diseases and Suggesting Pesticides

📌 Overview
The Plant Leaf Disease Detection System is a computer vision-based deep learning project designed to detect plant diseases from leaf images using Convolutional Neural Networks (CNNs). The system helps farmers and agricultural experts automatically classify plant diseases and recommends appropriate pesticides to mitigate the issue.

📌 Key Features:
✅ Image Classification – Detects plant diseases using deep learning
✅ Automated Pesticide Suggestion – Recommends suitable pesticides
✅ Graphical User Interface (GUI) – Built with Tkinter for easy usability
✅ Live Camera Capture & Image Upload – Allows capturing and analyzing images in real-time
✅ Preprocessing & Feature Extraction – Uses OpenCV and TensorFlow for image processing

🛠️ Technologies Used
Programming Language: Python 3.x
Machine Learning Framework: TensorFlow/Keras
Image Processing: OpenCV
GUI Development: Tkinter
Deep Learning Model: CNN (Convolutional Neural Networks)
Dataset: PlantVillage Dataset
📌 Features & Functionalities
1️⃣ User Features
Upload or capture an image of a plant leaf
Automatic preprocessing and feature extraction
Classification of the leaf as healthy or diseased
Displays the infected area percentage
Provides recommended pesticides based on disease type
2️⃣ Backend & Model Details
Uses a CNN-based classifier to recognize plant diseases
Implements image segmentation to detect infected areas
Thresholding & Contour Detection for leaf disease analysis
Tkinter-based GUI for easy accessibility
📌 How It Works
1️⃣ User uploads or captures an image of the plant leaf
2️⃣ Preprocessing: Image is resized, converted to grayscale, and noise is removed
3️⃣ Feature Extraction: The model detects infection areas using edge detection
4️⃣ Classification: The CNN model predicts the disease type
5️⃣ Output Display:

Shows the disease name
Calculates the infected area percentage
Displays suggested pesticides
📌 Installation & Setup
🔹 Prerequisites
Ensure you have the following installed:

Python 3.x
TensorFlow & Keras
OpenCV
PIL (Pillow)
Tkinter
NumPy

📌 Example Use Case
1️⃣ Select Image: Upload or capture an image
2️⃣ Analyze Image: The system classifies the plant leaf
3️⃣ Process Image: Detects infected area and displays results
4️⃣ Output:

Disease name
Infection percentage
Recommended pesticides
