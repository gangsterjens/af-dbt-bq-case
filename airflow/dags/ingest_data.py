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


def exec_task(ingest_arg: str, dag: DAG):
    """Helper to create DockerOperator tasks for each ingest type."""
    return DockerOperator(
        task_id=f"ingest_{ingest_arg}",
        image="dncase_ingest:latest",
        command=f"python handler.py {ingest_arg}",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment={
            "BQ_PROJECT": os.getenv("BQ_PROJECT", "dn-case-476208"),
            "BQ_DATASET": os.getenv("BQ_DATASET", "case_data_raw"),
        },
        dag=dag,
    )



ingest_articles = exec_task("articles", dag)
ingest_entities = exec_task("entities", dag)
ingest_keywords = exec_task("keywords", dag)
ingest_teaser = exec_task("teaser", dag)
ingest_gzip = exec_task("gzip", dag)



[ingest_gzip, ingest_articles, ingest_entities, ingest_keywords, ingest_teaser]
