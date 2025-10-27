# dbt/Dockerfile
FROM --platform=linux/amd64 ghcr.io/dbt-labs/dbt-bigquery:1.8.1

WORKDIR /app
COPY dbt_project.yml .
COPY profiles.yml .
COPY models ./models
COPY Data/creds ./Data/creds


ENV DBT_PROFILES_DIR=/app
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/Data/creds/dn-case-476208-b05c98ae2260.json

CMD ["dbt", "run"]
