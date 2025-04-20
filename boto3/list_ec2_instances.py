import boto3
import requests
import json
import logging

# Setup
region = "us-east-1"

# 3. List Running EC2 Instances
def list_ec2_instances():
    ec2 = boto3.client("ec2", region_name=region)
    instances = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    print("Running EC2 Instances:")
    for res in instances["Reservations"]:
        for inst in res["Instances"]:
            print(f" - {inst['InstanceId']} ({inst['InstanceType']})")

# MAIN
if __name__ == "__main__":
    list_ec2_instances()
