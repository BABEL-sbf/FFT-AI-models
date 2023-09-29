# Models for FFT

This repository contains tools and scripts for tracking fish in videos and identifying them using deep learning models. The main focus is on the YOLOv8 and EfficientNet models. Additionally, there's a utility script for exporting datasets from CoralNet.

Basic fish counter using yolov8 and bytetrack:

![fishcount](https://github.com/kluless13/FFT-AI-models/blob/main/YOLO/fishstock-result.gif)

## Table of Contents

- [YOLO](#yolo)
- [Efficients](#efficients)
- [Scripts](#scripts)
- [Model Information](#model-information)

## YOLO

### 1. YOLOv8

- **Description**: The YOLO folder contains the `tracker.py` script which implements the YOLOv8 model for object detection and provides tracking capabilities to count fish in video streams.

## Efficients

### 1. EfficientNet

- **Description**: The `efficients` folder contains scripts and utilities related to the EfficientNet model. It includes an implementation of the EfficientNet model architecture, originally from TensorFlow, ported to PyTorch.
- **Instructions**:
  1. Navigate to the `efficients` directory.
  2. Explore the `efficientnet-pytorch.py` for the PyTorch implementation of EfficientNet.

### 2. Exodus

- **Description**: The `exodus.py` script in the `efficients` folder is designed to download raw images from CoralNet.
- **Instructions**:
  1. Navigate to the `efficients` directory.
  2. Run the `exodus.py` script using the command `python exodus.py [OPTIONS]`.
  3. Replace `[OPTIONS]` with any command-line arguments or flags specific to the script.

## Model Information

### YOLOv8

- **Architecture**: YOLOv8 is an evolution of the YOLO architecture, focusing on real-time object detection. It divides images into a grid and predicts bounding boxes and class probabilities simultaneously.

### EfficientNet

- **Architecture**: EfficientNet scales the width, depth, and resolution of the network based on a compound coefficient, ensuring a balance between accuracy and computational resources.

---

