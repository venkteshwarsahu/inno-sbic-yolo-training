import os
import logging

logging.basicConfig(level=logging.INFO)

images_dir = "Aadhar card/old aadhar/images"
labels_dir = "Aadhar card/old aadhar/labels"

start_number = 4000

images = sorted([
    f for f in os.listdir(images_dir)
    if os.path.isfile(os.path.join(images_dir, f))
])

counter = start_number

for image_file in images:
    image_name, image_ext = os.path.splitext(image_file)

    label_file = image_name + ".txt"

    old_image_path = os.path.join(images_dir, image_file)
    old_label_path = os.path.join(labels_dir, label_file)

    new_base_name = str(counter)
    new_image_name = new_base_name + image_ext
    new_label_name = "image" + new_base_name + ".txt"

    new_image_path = os.path.join(images_dir, new_image_name)
    new_label_path = os.path.join(labels_dir, new_label_name)

    os.rename(old_image_path, new_image_path)

    if os.path.exists(old_label_path):
        os.rename(old_label_path, new_label_path)
    else:
        logging.warning(f"Warning: Label missing for {image_file}")

    logging.info(f"Renamed {image_file} → {new_image_name}")

    counter += 1

logging.info("Renaming completed.")
