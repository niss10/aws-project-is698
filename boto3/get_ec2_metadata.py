import boto3
import requests
import json
import logging

# Setup
region = "us-east-1"

# 2. Retrieve EC2 Metadata (run this on an EC2 instance only!)
def get_ec2_metadata():
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"AZ: {instance['Placement']['AvailabilityZone']}")


# MAIN
if __name__ == "__main__":
    get_ec2_metadata()      # Safe to comment out if not on EC2