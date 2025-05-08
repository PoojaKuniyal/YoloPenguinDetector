from ultralytics import YOLO

# Load a pretrained YOLOv8n model
# model = YOLO("yolov8n.yaml") # train the model from scratch then use this
# as i'm using CPU on my machine will use pre-trained model to reduce the epochs, speed up the processing time and improve accuarcy

# train the model
# results = model.train(data='config.yaml', epochs=100)

# use pre-trained model
model = YOLO('yolov8s.pt')  # use 'yolov8s.pt' if you have better CPU or can run on GPU

results = model.train(
    data="config.yaml",
    epochs=30,
    imgsz= 320,  #lower resolution from 416 to reduce computation
    batch= 4,          # reduce if running out of memory have kept 8 earlier
    workers=2,
    patience=5, #  stops training early if there's no improvement.
    device='cpu'      # or 'cuda' if on GPU
)
