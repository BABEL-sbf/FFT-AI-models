from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("wts.pt") # choose the weights from the train set

results = model.predict(source="path to test dataset", conf = 0.30, save=False)
