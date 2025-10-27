cd airflow
🪶 Airflow (Local Dev Setup)

This folder contains a lightweight, Docker-based Apache Airflow setup for local development and DAG testing.

🚀 Quickstart

Move into the Airflow folder

cd airflow


Start Airflow (first-time setup)

docker compose down -v     # Clean old containers and volumes
docker compose up -d       # Spin up Airflow (webserver + scheduler)


Access the Airflow web UI

URL → http://localhost:8080

Username → admin

Password → admin

View or add DAGs

Place DAG files in the airflow/dags/ directory.

Airflow automatically detects new DAGs — just refresh the web UI.