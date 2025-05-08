
# 🐧 Penguin Detection with YOLOv8

This repository contains an object detection pipeline using **YOLOv8** to detect **Penguins** (single class) in images. The dataset is sourced from the Open Images Dataset and are pre-annotated.

## 📁 Dataset

* **Training Images**: 600
* **Validation Images**: 41
* **Class**: Penguin (mapped to class `0`)
* Labels were normalized and converted to YOLO format.

## 🧠 Model Details

* **Base Model**: `yolov8s.pt` (pre-trained)
* **Training Epochs**: 30
* **Image Size**: 320
* **Device**: CPU 

## 📊 Results

| Metric        | Value |
| ------------- | ----- |
| Precision     | 0.332 |
| Recall        | 0.365 |
| mAP\@0.5      | 0.306 |
| mAP\@0.5:0.95 | 0.111 |


Bounding boxes are drawn around detected penguins in the output.<br>
Videos and image of the detected penguins are uploaded.

-----
"This model is still improving. Current results are modest due to dataset challenges (label quality, object size), and efforts are ongoing to optimize performance."
 
