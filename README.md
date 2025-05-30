📌 Project Overview
The Skin Cancer Detection Android App is a mobile-based AI solution designed to assist users in the early detection of skin cancer. By capturing or uploading skin lesion images, the app utilizes a Convolutional Neural Network (CNN) model to classify images and return predictions in real time.

🎯 Key Features
📷 Image Capture & Upload: Users can take a photo or select an image from their gallery.

🧠 CNN-based Detection: Integrated machine learning model trained on dermatology datasets.

🔁 Real-time Predictions: Backend Python model returns results instantly via API.

📱 User-Friendly UI: Clean and intuitive interface built with Android Studio.

🛠️ Technologies Used
Android (Java/Kotlin) – Frontend mobile development

Python – Backend model development

TensorFlow/Keras – Deep learning framework for CNN training

OpenCV – Image preprocessing and enhancement

Flask – Lightweight Python API to serve the model

REST API – Communication between Android frontend and Python backend

🧪 How It Works
User uploads or captures an image of the affected skin area.

The image is preprocessed and sent to a Flask-based Python API.

The trained CNN model analyzes the image and returns a prediction (e.g., benign or malignant).

The result is displayed to the user in the app interface.

🚀 Future Improvements
Integration of additional skin condition classifiers

Improved model accuracy using larger and more diverse datasets

Offline prediction support via TensorFlow Lite

Report generation and health tips for users                                                               
📊 Dataset
The model is trained on publicly available dermatology image datasets (https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset).                                                                                                                                    
