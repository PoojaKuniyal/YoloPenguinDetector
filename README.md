## 🐧 Object Detection (Penguin) using YOLOv8s – Improved GPU Training (colab)

This repository contains code and configuration for training a custom object detection model using [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics). The model detects penguins in images using a single class.

### 📁 Dataset

* **Source**: Open Images Dataset (OIDv6)
* **Class**: Penguin (`/m/0jbk`)
* **Train Images**: 600
* **Validation Images**: 41
* Data was preprocessed into YOLO format with normalized bounding boxes and class label `0`.

### 🏗️ Training Configuration (Latest Run)

* **Base Model**: `yolov8s.pt`
* **Epochs**: 200
* **Image Size**: 640×640
* **Batch Size**: 4
* **Device**: Tesla T4 (Colab GPU)
* **Early Stopping**: Disabled

### 📊 Evaluation Results

| Metric        | Value |
| ------------- | ----- |
| Precision (P) | 0.417 |
| Recall (R)    | 0.665 |
| mAP\@0.5      | 0.508 |
| mAP\@0.5:0.95 | 0.281 |

> 📝 Note: This improved result was obtained by training longer (200 epochs), using higher image resolution (640), and leveraging GPU acceleration on Google Colab.

# Earlier run on vscode

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

 
