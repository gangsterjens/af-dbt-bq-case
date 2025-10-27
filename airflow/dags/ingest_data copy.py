from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
import os


default_args = {
    "owner": "airflow",
    "retries": 0,
}


# Define the DAG
dag = DAG(
    dag_id="ingest_dag",
    default_args=default_args,
    description="Run DN-case ingestion pipeline for all sources",
    start_date=datetime(2025, 10, 1),
    schedule_interval=None,
    catchup=False,
)



dbt_run = DockerOperator(
    task_id="dbt_run",
    image="dncase_dbt:latest",
    command="run --select tag:mart",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    environment={
        "DBT_PROFILES_DIR": "/app",
        "GOOGLE_APPLICATION_CREDENTIALS": "/app/Data/creds/dn-case-476208-b05c98ae2260.json",
    },
    mounts=[],
    dag=dag)



[ingest_gzip, ingest_articles, ingest_entities, ingest_keywords, ingest_teaser] >> dbt_run
