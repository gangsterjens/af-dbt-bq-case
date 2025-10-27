{{ config(tags=['ingest'], materialized='view') }}


SELECT
  distinct 
  FARM_FINGERPRINT(concat(edition_id, published_at)) frontpage_id,
  edition_id,
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%E6S %Z', ingestiontime) as ingestion_time,
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S %Z', published_at) AS published_at,
  lantern_id,
  cast(position as integer) position,
  priority
FROM {{ source('case_data_raw', 'teaser_positions') }}






