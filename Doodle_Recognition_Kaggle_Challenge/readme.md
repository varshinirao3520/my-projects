📌 Overview
This project is a deep learning-based sketch classification system built for the Quick, Draw! Doodle Recognition Challenge. Using a Convolutional Neural Network (CNN), the model classifies sketches from a dataset of 50 million doodles across 340 categories. The challenge is to develop a robust classifier that can handle noisy, incomplete, and varied user-drawn sketches.

📌 Competition Rank: 171st out of 1309 submissions
📌 Final Model Accuracy: 93.17% Test Accuracy
📌 Dataset Used: Google Quick, Draw! Dataset

🚀 Features
✅ Deep Learning-Based Sketch Classification using CNN
✅ Optimized Image Preprocessing with NumPy bitmaps for efficiency
✅ Batch Normalization, Dropout, and Regularization for improved model generalization
✅ Adam Optimizer with Categorical Cross-Entropy Loss
✅ Data Augmentation to improve classification accuracy

🛠️ Technologies Used
Python 3.x
TensorFlow/Keras
NumPy & Pandas
OpenCV
Matplotlib & Seaborn
Google Quick, Draw! Dataset
Jupyter Notebook (for experimentation)
📌 Project Methodology
1️⃣ Data Preparation
Used NumPy bitmaps instead of CSV files for efficient image processing.
Preprocessed images by resizing them to 28x28 pixels and normalizing pixel values (0-1 range).
2️⃣ CNN Architecture
Convolutional Layers extract spatial features from sketches.
Batch Normalization stabilizes activations and improves training speed.
Max Pooling reduces dimensionality while preserving critical features.
Dropout Layers prevent overfitting by randomly deactivating neurons.
Fully Connected Layers classify sketches into one of 340 categories.
3️⃣ Training & Optimization
Loss Function: Categorical Cross-Entropy
Optimizer: Adam
Learning Rate Scheduling: Adaptive learning rate to improve convergence
Regularization: Dropout, Batch Normalization, L2 Regularization
4️⃣ Model Evaluation
Final Test Accuracy: 93.17%
Rank: 171st out of 1309 submissions on Kaggle
Best CNN-based models reached ~95.6% accuracy
📌 How to Run the Project
🔹 Prerequisites
Make sure you have Python and the required libraries installed:

pip install numpy pandas tensorflow keras opencv-python matplotlib seaborn

🔹 Clone the Repository

git clone https://github.com/varshinirao3520/my-projects/new/main/Doodle_Recognition_Kaggle_Challenge.git
cd quick-draw-sketch-classifier

🔹 Run the Jupyter Notebook

jupyter notebook
Open ml_fpga_project_final.ipynb and run all cells to train & evaluate the model.
