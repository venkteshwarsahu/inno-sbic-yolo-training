import os
import logging

logging.basicConfig(level=logging.INFO)

images_dir = "Aadhar card/old aadhar/images" 

for filename in os.listdir(images_dir):
    old_path = os.path.join(images_dir, filename)

    if not os.path.isfile(old_path):
        continue

    name, ext = os.path.splitext(filename)
    new_name = f"image{name}{ext}"
    new_path = os.path.join(images_dir, new_name)

    os.rename(old_path, new_path)
    logging.info(f"{filename} → {new_name}")

logging.info("Renaming completed.")
