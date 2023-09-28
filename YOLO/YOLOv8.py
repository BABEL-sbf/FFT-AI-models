# FFor notebookks

# Installing dependencies

%!nvidia-smi

import os
HOME = os.getcwd()
print(HOME)

!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

!mkdir {HOME}/datasets
%cd {HOME}/datasets

!pip install roboflow

from roboflow import Roboflow
#Roboflow API

# Model Training (YOLOv8s)

%cd {HOME}

!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=75 imgsz=800 plots=True
!ls {HOME}/runs/detect/train/
Image(filename=f'{HOME}/runs/detect/train/confusion_matrix.png', width=600)
Image(filename=f'{HOME}/runs/detect/train/F1_curve.png', width=600)
Image(filename=f'{HOME}/runs/detect/train/results.png', width=600)

# Model Validation

%cd {HOME}

!yolo task=detect mode=val model={HOME}/runs/detect/train/weights/best.pt data={dataset.location}/data.yaml 
!ls {HOME}/runs/detect/val/
Image(filename=f'{HOME}/runs/detect/val/confusion_matrix.png', width=600)
Image(filename=f'{HOME}/runs/detect/val/F1_curve.png', width=600)
Image(filename=f'{HOME}/runs/detect/val/val_batch0_pred.jpg', width=600)

# Model Prediction

%cd {HOME}

!yolo task=detect mode=predict model={HOME}/runs/detect/train/weights/best.pt conf=0.25 source={dataset.location}/test/images save=True

import glob
from IPython.display import Image, display

for image_path in glob.glob(f'{HOME}/runs/detect/predict/*.jpg')[:3]:
      display(Image(filename=image_path, width=600))
      print("\n")
