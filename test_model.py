# this code not required have written just to check if the model is
# technically working as my model was unable to detect object in the video
# The model is:
#Outputting bounding boxes,
# But it's not confident at all, meaning it hasn’t actually learned meaningful features from data.
# as model is severely undertrained.

from ultralytics import YOLO  # or use torch.hub if YOLOv5
import cv2

model = YOLO("C:/Users/Lenovo/YoloPenguin/runs/detect/train13/weights/last.pt")  # adjust path if needed
results = model.predict(source=r"C:\Users\Lenovo\OneDrive\Desktop\RadhaMadhav\Penguin2.mp4", conf=0.001, save=True)

# Optionally visualize
img = cv2.imread(r"C:\Users\Lenovo\OneDrive\Desktop\RadhaMadhav\Penguin2.mp4")
for r in results:
    boxes = r.boxes
    print("Detected:", len(boxes))
    for box in boxes:
        print(box.xyxy, box.conf, box.cls)
