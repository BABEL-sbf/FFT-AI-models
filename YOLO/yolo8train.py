
from ultralytics import YOLO

model = YOLO("yolo8n.pt) # choosing yolo model - n,s,m,l,x

#  model training
model.train(data = "data.yaml", epochs = 25) 
