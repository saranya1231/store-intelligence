from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="sample_data/test.jpg",
    save=True
)

print("Detection completed")