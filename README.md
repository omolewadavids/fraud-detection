# Fraud Detection Model with CI/CD Pipeline on AWS

This repository contains a **Fraud Detection model** using synthetic tabular data, deployed as a containerized FastAPI application using Docker, with CI/CD pipeline integration to AWS using **Terraform** and **GitHub Actions**.

The project includes:
- **Synthetic Data Generation**: Generating normal and fraudulent transaction data.
- **Data Preprocessing**: Preparing data for model training.
- **Model Training**: Training a model using machine learning algorithms.
- **Model Deployment**: Deploying the trained model on AWS using **ECS**, **ECR**, and **Fargate**.
- **CI/CD Pipeline**: Automating deployment using GitHub Actions and Terraform.

---

## Project Structure

```plaintext
fraud-detection/
├── app/
│   ├── Dockerfile                # Dockerfile for the FastAPI app
│   ├── main.py                   # FastAPI app
│   ├── model.py                  # Fraud detection model
│   └── requirements.txt          # Python dependencies for the FastAPI app
├── data/
│   └── generate_data.py          # Script to generate synthetic fraud detection data
├── infrastructure/
│   ├── main.tf                   # Terraform configuration for AWS resources
│   ├── variables.tf              # Terraform variables
│   ├── outputs.tf                # Terraform outputs
│   └── provider.tf               # AWS provider setup for Terraform
└── .github/
    └── workflows/
        └── ci/cd.yml            # CI/CD GitHub Actions workflow
