{{ config(tags=['ingest'], materialized='table') }}


SELECT
  content_id as lantern_id,
  cast(partitiondate as date) as partitiondate,
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S %Z', partitionhour) AS partitionhour,
  sum(pageviews) as pageviews,
  sum(user_reads60) as user_reads60
FROM {{ source('case_data_raw', 'segment_stats') }}
group by 1, 2, 3






