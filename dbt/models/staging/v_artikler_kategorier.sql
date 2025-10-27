{{ config(tags=['ingest'], materialized='view') }}


SELECT
  lantern_id, 
  category,
  category_name,
  cast(is_default as boolean) as is_default
FROM {{ source('case_data_raw', 'artikler_kategorier') }}
