{{ config(tags=['ingest'], materialized='view') }}


SELECT
  lantern_id, 
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%E6S %Z', ingestion_time) as ingestion_time,
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%E6S %Z', published_at) as published_at,
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%E6S %Z', updated_date) as updated_date,
  lead_text,
  title
FROM {{ source('case_data_raw', 'artikler_hoved') }}



