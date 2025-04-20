import boto3

# Setup
region = "us-east-1"
bucket_name = "boto3-created-bucket-demo-nisarg"
file_name = "boto3-upload.txt"
lambda_function_name = "s3-upload-logger-dev"

# 1. Create S3 Bucket and Upload a File
def create_and_upload_s3():
    s3 = boto3.client('s3', region_name=region)

    # Create Bucket
    try:
        s3.create_bucket(
            Bucket=bucket_name
        )
        print(f"Created bucket: {bucket_name}")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print("Bucket already exists.")

    # Upload a file
    with open(file_name, "w") as f:
        f.write("Hello from Boto3 upload!")

    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Uploaded {file_name} to {bucket_name}")

# MAIN
if __name__ == "__main__":
    create_and_upload_s3()
