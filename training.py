from ultralytics import YOLO
import logging
logging.basicConfig(level=logging.INFO)

logging.info("Training model...")
model = YOLO("yolo26s.pt")
train_results = model.train(
    data="aadhaar-classification-dataset/aadhaar.yaml",
    epochs=200,
    imgsz=640,
    device="0",
)

metrics = model.val()
logging.info("Validation metrics:")
logging.info(metrics)
results = model("image402.jpg")
logging.info("Results:")
logging.info(results)


# path = model.export(format="onnx")
# logging.info(f"Model exported to {path}")