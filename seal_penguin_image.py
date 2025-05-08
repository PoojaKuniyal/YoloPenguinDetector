import os
import cv2
from ultralytics import YOLO
from pathlib import Path

# Define image path
IMAGES_DIR = os.path.join('.', r"C:\Users\Lenovo\OneDrive\Desktop\RadhaMadhav")
image_path = os.path.join(IMAGES_DIR, 'seal_penguin.jpg')
image_path_out = '{}_out.jpg'.format(image_path)

# Load image
frame = cv2.imread(image_path)
H, W, _ = frame.shape

# Load YOLO model
model_path = Path(r'C:\Users\Lenovo\YoloPenguin\runs\detect\train3\weights\best.pt')
model = YOLO(model_path)  # Load custom model

threshold = 0.25

# Run YOLO model on the image
results = model(frame)[0]

# Draw bounding boxes
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

        cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1-10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# Save the processed image
cv2.imwrite(image_path_out, frame)

# Display result (optional)
cv2.imshow("Processed Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()