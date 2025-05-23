import os
from ultralytics import YOLO
import cv2

VIDEOS_DIR = os.path.join('.',r"C:\Users\Lenovo\OneDrive\Desktop\RadhaMadhav")
video_path = os.path.join(VIDEOS_DIR,'Penguin3.mp4')

video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame= cap.read()
H,W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

#model_path = os.path.join('.','C:\Users\Lenovo\YoloPenguin\runs','C:\Users\Lenovo\YoloPenguin\runs\detect','C:\Users\Lenovo\YoloPenguin\runs\detect\train13','C:\Users\Lenovo\YoloPenguin\runs\detect\train13\weights','C:\Users\Lenovo\YoloPenguin\runs\detect\train13\weights\last.pt')
from pathlib import Path
model_path = Path(r'C:\Users\Lenovo\YoloPenguin\runs\detect\train3\weights\best.pt')

# Load a model
model = YOLO(model_path) # load a custom model
threshold =0.25

while ret:
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1-10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()


cap.release()
out.release()
cv2.destroyAllWindows() 