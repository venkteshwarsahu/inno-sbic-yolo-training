import os
import boto3
import logging

logging.basicConfig(level=logging.INFO)

LOCAL_FOLDER = "dataset"
BUCKET_NAME = "testsbmaskevent"       
S3_PREFIX = "sbic/aadhaar-masking-dataset"

s3 = boto3.client("s3")

def upload_folder(local_folder, bucket, s3_prefix=""):
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)

            relative_path = os.path.relpath(local_path, local_folder)
            s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            logging.info(f"Uploading {local_path} -> s3://{bucket}/{s3_path}")

            try:
                s3.upload_file(local_path, bucket, s3_path)
            except Exception as e:
                logging.error(f"Failed to upload {local_path}: {e}")

# Run upload
upload_folder(LOCAL_FOLDER, BUCKET_NAME, S3_PREFIX)

logging.info("Upload completed")
