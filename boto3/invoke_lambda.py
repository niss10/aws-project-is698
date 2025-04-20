import boto3
import requests
import json
import logging

# Setup
region = "us-east-1"
lambda_function_name = "s3-upload-logger-dev"

# 4. Invoke Lambda Function Manually
def invoke_lambda():
    lambda_client = boto3.client("lambda", region_name=region)
    response = lambda_client.invoke(
        FunctionName=lambda_function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps({})
    )
    result = response['Payload'].read().decode('utf-8')
    print(f"Lambda invocation result: {result}")

# MAIN
if __name__ == "__main__":
    invoke_lambda()
