# Baseball Data Pipeline

This project is a baseball data pipeline that ingests Statcast data, processes it, and visualizes it on a dashboard. The project includes scripts for:

- Ingesting raw baseball data from APIs.
- Processing and cleaning the data.
- Storing the data in a PostgreSQL database.
- Visualizing the data in a Dash dashboard.

## Table of Contents
1. [Setup](#setup)
2. [Running the Pipeline](#running-the-pipeline)
3. [Docker Setup (Optional)](#docker-setup-optional)
4. [Kubernetes Deployment (Azure)](#kubernetes-deployment-azure)
5. [Testing](#testing)

## Setup

### 1. Install dependencies
Run:

```bash
pip install -r requirements.txt
```

### 2. Set up the PostgreSQL database
If you don't have PostgreSQL installed, you can follow the [PostgreSQL Installation Guide](https://www.postgresql.org/download/) to set it up. Once installed, run the `setup_database.sql` script in your PostgreSQL instance:
```bash
psql -f setup_database.sql
```

### 3. Environment Variables
Ensure you have the following environment variables set up in your environment:
- **DATABASE_URL**: Connection string for your PostgreSQL database, formatted as:
```bash
postgresql://username:password@hostname:5432/mydatabase
```

You can set the environment variable in your terminal like this:
```bash
export DATABASE_URL="postgresql://username:password@hostname:5432/mydatabase"
```

## Run the pipeline

### 1. Ingest Statcast data
Run the data ingestion script:
```bash
python ingestion/ingest_data.py
```

### 2. Process the ingested data and save it to the database
Run the data processing script:
```bash
python processing/process_data.py
```

### 3. Start the dashboard
Run the dashboard with:
```bash
python app.py
```
The dashboard will be available at http://localhost:8050

## Docker Setup (Optional)
o run the pipeline in a Docker container, ensure you have Docker installed. Follow the [Docker Installation Guide](https://docs.docker.com/get-docker/) to install Docker on your machine. Then, build and run the Docker image:

### 1. Build the Docker image
```bash
docker build -t baseball-pipeline -f deployment/Dockerfile
```

### 2. Run the Docker container
```bash
docker run -p 8050:8050 baseball-pipeline
```

## Kubernetes Deployment (Azure)
To deploy the pipeline on Azure Kubernetes Service (AKS), follow these steps:

### 1. Deployment Script
Run the following script to automate the creation of the AKS cluster and deployment of the application:
```bash
./deploy_aks.sh
```

### 2. Make the script executable
To make the script executable, run:
```bash
chmod +x deploy_aks.sh
```

#### Note:
Ensure that placeholder values in the deploy_aks.sh script are replaced with your actual Azure resource group, cluster name, and database connection string.

## Testing
To run unit tests for the pipeline:
```bash
python -m unittest tests/test_pipeline.py
```