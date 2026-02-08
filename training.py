from ultralytics import YOLO
import logger


model = YOLO("yolo26s.pt")
train_results = model.train(
    data="aadhaar-classification-dataset/aadhaar.yaml",
    epochs=100,
    imgsz=640,
    device="cpu",
)

metrics = model.val()
logger.info(metrics)
results = model("image402.jpg")
logger.info(results)
path = model.export(format="onnx")
logger.info(f"Model exported to {path}")