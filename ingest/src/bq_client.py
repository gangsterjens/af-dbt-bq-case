from google.cloud import bigquery
import pandas as pd
import os
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

class BQClient:
    def __init__(self, app_json: str, bq_project: str, bq_dataset: str):
        # Set credentials for BigQuery
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = app_json
        self.client = bigquery.Client(project=bq_project)
        self.table_prefix = f"{bq_project}.{bq_dataset}"

    def upload_df(self, df: pd.DataFrame, table_name: str, mode: str = "WRITE_TRUNCATE"):
        """Upload a DataFrame to BigQuery.
        
        Args:
            df (pd.DataFrame): DataFrame to upload
            table_name (str): Table name (no dataset prefix)
            mode (str): WRITE_TRUNCATE (overwrite), WRITE_APPEND, or WRITE_EMPTY
        """
        table_id = f"{self.table_prefix}.{table_name}"
        job_config = bigquery.LoadJobConfig(write_disposition=mode)

        job = self.client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()  # Wait for upload to complete

        print(f"✅ Uploaded {len(df)} rows to BigQuery: {table_id}")

    def list_tables(self):
        """List all tables in the dataset."""
        tables = list(self.client.list_tables(self.table_prefix))
        return [t.table_id for t in tables]

    def query(self, sql: str) -> pd.DataFrame:
        """Run a query and return as DataFrame."""
        return self.client.query(sql).to_dataframe()
