# Models fo FFT

This repository contains detailed notebooks for YOLOv8, EfficientNet, EfficientDet, and Faster R-CNN models. 
Additionally, there's a utility script for exporting datasets from CoralNet.

## Table of Contents

- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Model Information](#model-information)

## Notebooks

### 1. YOLOv8 Notebook

- **Description**: This notebook provides a comprehensive guide to the YOLOv8 model, which is known for its 
real-time object detection capabilities.
- **Instructions**:
  1. Ensure you have the required dependencies installed.
  2. Open the notebook in Jupyter or any compatible environment.
  3. Follow the step-by-step instructions and execute each cell in sequence.

### 2. EfficientNet Notebook

- **Description**: Dive into the EfficientNet model, designed for high accuracy in image classification tasks 
with efficient computational resource usage.
- **Instructions**:
  1. Install necessary libraries and dependencies.
  2. Launch the notebook and go through each section to understand the model's architecture and 
implementation.

### 3. EfficientDet Notebook

- **Description**: Explore the EfficientDet model, an object detection model that balances accuracy and 
efficiency.
- **Instructions**:
  1. Setup the environment as per the initial cells in the notebook.
  2. Execute the cells in order to train or test the model on your dataset.

### 4. Faster R-CNN Notebook

- **Description**: Delve into the Faster R-CNN model, a pioneering model in object detection with Region 
Proposal Networks.
- **Instructions**:
  1. Ensure the dataset is in the required format.
  2. Follow the notebook to train and evaluate the Faster R-CNN model on your data.

## Scripts

### exodus.py

- **Description**: A utility script designed to export datasets from CoralNet seamlessly.
- **Instructions**:
  1. Ensure you have the necessary permissions to access the datasets on CoralNet.
  2. Run the script using `python exodus.py` (or the appropriate command for your environment).
  3. Follow any on-screen prompts to complete the export process.

## Model Information

### YOLOv8

- **Architecture**: YOLOv8 is an evolution of the YOLO architecture, focusing on real-time object detection. 
It divides images into a grid and predicts bounding boxes and class probabilities simultaneously.

### EfficientNet

- **Architecture**: EfficientNet scales the width, depth, and resolution of the network based on a compound 
coefficient, ensuring a balance between accuracy and computational resources.

### EfficientDet

- **Architecture**: EfficientDet is an object detection model that uses a compound scaling method, similar to 
EfficientNet, to uniformly scale the resolution, depth, and width for all backbone, feature network, and 
box/class prediction networks.

### Faster R-CNN

- **Architecture**: Faster R-CNN introduces the Region Proposal Network (RPN) that shares full-image 
convolutional features with the detection network, thus enabling nearly cost-free region proposals.

---
