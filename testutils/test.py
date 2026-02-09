import os
import logging

logging.basicConfig(level=logging.INFO)

images_dir = "Aadhar-data/new aadhar/aadhaar-masking-temp/images/val"
labels_dir = "Aadhar-data/new aadhar/aadhaar-masking-temp/labels/val"

image_files = {os.path.splitext(f)[0] for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))}
label_files = {os.path.splitext(f)[0] for f in os.listdir(labels_dir) if os.path.isfile(os.path.join(labels_dir, f))}

missing_labels = image_files - label_files
missing_images = label_files - image_files

logging.info("Images without labels:")
for name in sorted(missing_labels):
    logging.info(name)

logging.info("\nLabels without images:")
for name in sorted(missing_images):
    logging.info(name)
