# DN-Case

### Three docker images, one ingest-image, one dbt-image. and a airflow-image that orchestrates the two images


## The solution is drawed below
<img width="1078" height="455" alt="Skjermbilde 2025-10-27 kl  22 29 55" src="https://github.com/user-attachments/assets/eee6b37a-01f1-4eec-a47a-2eb20330109f" />


# NB! To run the model you need a json-key to authenticate with GCP

This is naturally in .gitignore
but must be stored under ingest/Data/creds/creds.json
the file must also be put into dbt-folder
