from ultralytics import YOLO
import logging
import cv2
logging.basicConfig(level=logging.INFO)

model = YOLO("model/best.pt")
results = model("image402.jpg")

logging.info(results[0])
result = results[0]
logging.info(result)
logging.info(result.boxes.xyxy)   # bounding box coordinates
logging.info(result.boxes.conf)   # confidence
logging.info(result.boxes.cls)    # class id

# Draw bounding boxes on image
annotated_img = result.plot()

# Save image
output_path = "image402_with_boxes.jpg"
cv2.imwrite(output_path, annotated_img)

logging.info(f"Saved annotated image at: {output_path}")