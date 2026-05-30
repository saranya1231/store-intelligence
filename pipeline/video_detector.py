import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("data/sample.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    print(results)

cap.release()