# Designing and Implementing a Scalable Cloud Architecture on AWS

This project demonstrates the design and implementation of a scalable, secure, and event-driven cloud architecture on AWS using a combination of **Terraform**, **AWS CloudFormation**, **AWS CLI**, **Boto3 (Python)**, and **GitHub** for version control. It follows Infrastructure-as-Code (IaC) and DevOps best practices to provision and automate all core components of a modern web application infrastructure.

---

## Objectives

- Design a fault-tolerant and scalable architecture with high availability
- Deploy infrastructure components using **Terraform** and **CloudFormation**
- Use **Lambda** to respond to **S3 file upload events**
- Perform **EC2, S3, and Lambda operations using AWS CLI**
- Automate AWS operations using **Python and Boto3**
- Track all code in **GitHub** for reproducibility and collaboration

---

## Architecture Overview

The architecture includes the following components:

- **VPC** with public and private subnets in multiple AZs (Terraform)
- **EC2 instances** behind an **Application Load Balancer (ALB)** with Auto Scaling (CloudFormation)
- **RDS (MySQL)** deployed in private subnets (CloudFormation)
- **S3 bucket** for storing logs and triggering events (CloudFormation)
- **Lambda function** triggered on S3 file uploads, logging to CloudWatch (CloudFormation)
- **Security Groups** for EC2, ALB, and RDS with strict inbound/outbound rules
- **CLI and Boto3 scripting** to interact with deployed infrastructure
- **Architecture diagram** created in draw.io

---

## Infrastructure Deployment

### Terraform (`terraform/`)
Terraform is used for the networking layer:
- VPC (`scalable-vpc`)
- Public Subnets in `us-east-1a`, `us-east-1b`
- Private Subnets in `us-east-1a`, `us-east-1b`
- Internet Gateway and Public Route Table
- Security Groups for ALB (`alb-sg`), EC2 (`ec2-sg`), and RDS (`rds-sg`)

Outputs from Terraform (VPC ID, Subnet IDs, SG IDs) are used as parameters in CloudFormation.

### CloudFormation (`cloudformation/`)
CloudFormation templates were split by layer:

1. **EC2 + ALB + Auto Scaling**:
   - Launch Template with UserData for Apache install
   - ALB and Target Group
   - Auto Scaling Group across public subnets

2. **RDS**:
   - MySQL DB instance across private subnets
   - DBSubnetGroup
   - Attached to RDS SG

3. **Lambda + S3 Logging**:
   - S3 Bucket (`scalable-logs-bucket-dev`)
   - Lambda function to log uploads
   - IAM Role and Permission
   - Manual trigger configuration in S3 (due to CloudFormation limitations)

---

## Manual Configurations (Post-Deployment)

- **S3 to Lambda trigger** was manually configured via AWS Console → S3 → Properties → Event Notifications → Add Lambda function
- Verified all infrastructure components using AWS Console

---

## AWS CLI Interactions (`cli_commands/`)
Used AWS CLI to perform and verify:

- List all S3 buckets
- Upload a file to S3
- List all running EC2 instances
- Invoke Lambda function manually

---

## Boto3 Automation (`boto3/aws_interactions.py`)
Created a single Python script that performs:

- Create a new S3 bucket and upload a file
- Retrieve EC2 metadata (from within EC2 instance)
- List all running EC2 instances
- Invoke a Lambda function manually

---

## Architecture Diagram

The architecture was designed using **draw.io**, showing all core AWS components and their relationships:
- VPC, subnets, ALB, EC2, RDS, S3, Lambda
- Data flow arrows and public/private segmentation

Diagram file included: `/architecture/aws_architecture.drawio`

---

## Project Structure
```AWS-PROJECT-IS698/
├── terraform/
│   └── main.tf
├── cloudformation/
│   └── infra.yaml
├── boto3/
│   └── scripts.py
├── architecture/
│   └── aws_architecture.drawio
├── cli_commands/
│   └── cli.txt
├── README.md
```

---

## Security Best Practices Followed

- Least privilege IAM role for Lambda
- No hardcoded credentials (used `aws configure`)
- All access to RDS limited to EC2 SG only
- Public access disabled for private subnets and RDS

---

## Future Improvements

- Add CI/CD pipeline (CodePipeline or GitHub Actions)
- Integrate with API Gateway and Step Functions
- Add custom domain and SSL via ACM + Route53
- Use Systems Manager (SSM) for EC2 access

---

## Credits

This project was designed and implemented by **Nisarg Patel** as part of an end-to-end cloud architecture learning journey in the IS-698 Cloud Computing course, under the guidance of **Dr. Samson Oni**.

---

## License

This project is for educational and demonstration purposes.
