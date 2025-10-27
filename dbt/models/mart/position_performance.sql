{{ config(tags=['mart'], materialized='table') }}
with t1 as (
select 
  (FLOOR(position / 10) * 10) AS position_bucket,
  lantern_id,
  min(published_at) AS min_published_at,
  max(published_at) as max_published_at
FROM {{ ref('v_teaser_positions') }}
group by 1, 2
order by lantern_id)
select 
  t1.lantern_id, 
  position_bucket,
  sum(pageviews) pageviews,
  sum(user_reads60) user_reads60,
  sum(user_reads60) / sum(pageviews)  prct_read_60
FROM t1 
join {{ ref('aggr_segment_stats') }} ss
  on t1.lantern_id = ss.lantern_id and ss.partitionhour between t1.min_published_at and t1.max_published_at
group by 1, 2
order by t1.lantern_id, t1.position_bucket
