from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Import your project’s functions for each stage
from ingestion import ingest_data
from processing import process_data
from models.train_model import train_model
from monitoring.monitor_model import monitor_model

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'ml_pipeline_dag',
    default_args=default_args,
    description='Machine Learning Pipeline Orchestration',
    schedule_interval=timedelta(days=1),  # Run once a day
    catchup=False,
) as dag:
    
    # Define tasks
    ingest_data_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
    )

    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    monitor_model_task = PythonOperator(
        task_id='monitor_model',
        python_callable=monitor_model,
    )

    # Set task dependencies
    ingest_data_task >> process_data_task >> train_model_task >> monitor_model_task
