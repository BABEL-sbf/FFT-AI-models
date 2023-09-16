# Object Detection and Classification in Marine Survey

Object detection and classification are two fundamental tasks in computer vision. 
While object detection involves identifying the presence and location of certain 
objects within an image, classification assigns a label to a detected object based on 
its category.

## Applications in Marine Survey

### Object Detection:
- **Marine Life Monitoring**: Detecting the presence of marine species such as fish, 
whales, or coral reefs in underwater images.
- **Ship and Submarine Detection**: Identifying the presence of ships or submarines 
in satellite or aerial images.
- **Underwater Equipment Inspection**: Detecting and locating underwater equipment 
like pipelines, cables, or sunken artifacts.

### Classification:
- **Species Classification**: Once a marine species is detected, classifying it into 
its specific species category.
- **Health Assessment**: Classifying the health of coral reefs or other marine 
ecosystems based on visual cues.
- **Water Quality Assessment**: Classifying water quality based on visual properties 
like turbidity or the presence of algae.

## Popular Models and Their Applications in Marine Survey

### EfficientNet:
- **Overview**: EfficientNet is a model designed for image classification that scales 
the depth, width, and resolution of the network.
- **Application**: Efficient for classifying marine species or assessing the health 
of marine ecosystems.

### EfficientDet:
- **Overview**: EfficientDet is an object detection model that builds upon the 
EfficientNet architecture.
- **Application**: Useful for detecting marine life or underwater equipment with high 
accuracy.

### Faster R-CNN:
- **Overview**: Faster R-CNN is an advanced object detection model that uses Region 
Proposal Networks (RPN) to extract potential bounding boxes.
- **Application**: Ideal for detecting and classifying marine species in 
high-resolution images.

### YOLO (You Only Look Once):
- **Overview**: YOLO is a real-time object detection system that divides the image 
into a grid and predicts bounding boxes and class probabilities simultaneously.
- **Application**: Due to its real-time capabilities, YOLO is suitable for monitoring 
marine activities in real-time, such as tracking marine species or detecting 
unauthorized fishing activities.
- **Advantage**: YOLO is known for its speed, making it ideal for real-time 
detection, especially when compared to models like Faster R-CNN.


---

| Model Name   | Use Case in Marine Survey                                                                                         
|
|--------------|--------------------------------------------------------------------------------------------------------------------|
| EfficientNet | Classifying marine species or assessing the health of marine 
ecosystems.                                           |
| EfficientDet | Detecting marine life or underwater equipment with high accuracy.                                                  
|
| Faster R-CNN | Detecting and classifying marine species in high-resolution images.                                                
|
| YOLO         | Monitoring marine activities in real-time, such as tracking marine 
species or detecting unauthorized fishing activities. |

## Conclusion

While YOLO stands out for real-time detection, models like EfficientDet and Faster 
R-CNN offer high accuracy. The choice of model largely depends on the specific 
requirements of the marine survey task. With tools like TensorFlow Lite, even 
resource-intensive models can be optimized for real-time applications.
