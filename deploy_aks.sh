#!/bin/bash

# Variables
RESOURCE_GROUP="myResourceGroup"
CLUSTER_NAME="myAKSCluster"
LOCATION="eastus"
DB_CONNECTION_STRING="postgresql://username:password@localhost:5432/baseball"

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

# Deploy Application
echo "Deploying application..."
kubectl apply -f deployment.yml

# Expose Application
echo "Creating service..."
kubectl apply -f service.yml

# Get External IP
echo "Fetching external IP..."
EXTERNAL_IP=""
while [ -z "$EXTERNAL_IP" ]; do
    EXTERNAL_IP=$(kubectl get services | grep baseball-pipeline-service | awk '{print $4}')
    echo "Waiting for external IP..."
    sleep 10
done

echo "Application is running. Access it at http://$EXTERNAL_IP"
