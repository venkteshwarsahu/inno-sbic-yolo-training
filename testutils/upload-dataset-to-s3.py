import os
import boto3
import logging

logging.basicConfig(level=logging.INFO)

LOCAL_FOLDER = "aadhaar-classification-dataset"
BUCKET_NAME = "testsbmaskevent"
S3_PREFIX = "sbic/aadhaar-classification-dataset"

s3 = boto3.client("s3")


def count_files(local_folder):
    total = 0
    for _, _, files in os.walk(local_folder):
        total += len(files)
    return total


def upload_folder(local_folder, bucket, s3_prefix=""):
    total_files = count_files(local_folder)
    uploaded_files = 0

    logging.info(f"Total files to upload: {total_files}")

    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)

            relative_path = os.path.relpath(local_path, local_folder)
            s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            try:
                s3.upload_file(local_path, bucket, s3_path)
                uploaded_files += 1
                logging.info(
                    f"Uploaded {uploaded_files}/{total_files} -> s3://{bucket}/{s3_path}"
                )

            except Exception as e:
                logging.error(f"Failed to upload {local_path}: {e}")

    logging.info(f"Upload completed: {uploaded_files}/{total_files} files uploaded")


# Run upload
upload_folder(LOCAL_FOLDER, BUCKET_NAME, S3_PREFIX)
