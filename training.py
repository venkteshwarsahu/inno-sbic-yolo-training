from ultralytics import YOLO
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting training")
model = YOLO("yolo26s.pt")
train_results = model.train(
    data="aadhaar-classification-dataset/aadhaar.yaml",
    epochs=100,
    imgsz=640,
    device="cpu",
)

metrics = model.val()
logging.info(metrics)
results = model("image402.jpg")
logging.info(results)
path = model.export(format="onnx")
logging.info(f"Model exported to {path}")