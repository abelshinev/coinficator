import ultralytics
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data=r"data.yaml", epochs=10)

