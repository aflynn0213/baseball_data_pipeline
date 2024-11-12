#!/bin/bash

set -e  # Stop the script if any command fails

# Variables
RESOURCE_GROUP="myResourceGroup"
CLUSTER_NAME="myAKSCluster"
LOCATION="eastus"
DB_CONNECTION_STRING="postgresql://username:password@localhost:5432/baseball"

# Functions
function check_prerequisites() {
    command -v az >/dev/null 2>&1 || { echo "Azure CLI is required but not installed. Aborting." >&2; exit 1; }
    command -v kubectl >/dev/null 2>&1 || { echo "kubectl is required but not installed. Aborting." >&2; exit 1; }
}

# Prerequisites Check
check_prerequisites

# Login to Azure
echo "Logging into Azure..."
az login

# Create Resource Group
echo "Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create AKS Cluster
echo "Creating AKS cluster..."
az aks create --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME --node-count 1 --enable-addons monitoring --generate-ssh-keys

# Get AKS Credentials
echo "Getting AKS credentials..."
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME

# Create Namespace (optional)
echo "Creating namespace..."
kubectl create namespace baseball-pipeline

# Deploy Application
echo "Deploying application..."
kubectl apply -f kubernetes/postgres-deployment.yaml -n baseball-pipeline
kubectl apply -f kubernetes/postgres-service.yaml -n baseball-pipeline
kubectl apply -f kubernetes/postgres-pvc.yaml -n baseball-pipeline
kubectl apply -f kubernetes/airflow-deployment.yaml -n baseball-pipeline
kubectl apply -f kubernetes/airflow-service.yaml -n baseball-pipeline

# Expose Application
echo "Creating service..."
kubectl apply -f kubernetes/service.yml -n baseball-pipeline

# Deploy Spark Operator (required for managing Spark jobs on Kubernetes)
echo "Deploying Spark Operator..."
kubectl apply -f https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/releases/download/v1beta2-1.2.3/spark-operator.yaml -n baseball-pipeline

# Deploy Spark job on AKS
echo "Deploying Spark job..."
kubectl apply -f kubernetes/spark-application.yaml -n baseball-pipeline

# Wait for External IP
echo "Fetching external IP..."
EXTERNAL_IP=""
while [ -z "$EXTERNAL_IP" ]; do
    EXTERNAL_IP=$(kubectl get services -n baseball-pipeline | grep baseball-pipeline-service | awk '{print $4}')
    echo "Waiting for external IP..."
    sleep 10
done

echo "Application is running. Access it at http://$EXTERNAL_IP"
