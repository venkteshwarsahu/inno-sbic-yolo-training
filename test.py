from ultralytics import YOLO
import logging

logging.basicConfig(level=logging.INFO)

model = YOLO("yolo26s.pt")
results = model("image402.jpg")

logging.info(results)