import cv2
import pandas as pd
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

videos = [
    "data/CAM1.mp4",
    "data/CAM2.mp4",
    "data/CAM3.mp4",
    "data/CAM4.mp4",
    "data/CAM5.mp4"
]

results_data = []

for video in videos:

    cap = cv2.VideoCapture(video)
    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 30 != 0:
            continue

        results = model(frame, verbose=False)

        person_count = sum(
            1 for box in results[0].boxes
            if int(box.cls[0]) == 0
        )

        results_data.append([
            video,
            frame_count,
            person_count
        ])

    cap.release()

df = pd.DataFrame(
    results_data,
    columns=["Camera", "Frame", "PersonCount"]
)

df.to_csv("person_counts.csv", index=False)

print("Saved person_counts.csv")