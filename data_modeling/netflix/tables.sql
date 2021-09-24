/*
Your mission is to build an ETL process to populate a dashboard that shows the top movies viewed for a streaming movie service.

Imagine we have a logging system in place that captures user playback events such as:
(userid, movieid, PLAYBACK_STARTED, movie_pos_in_secs, utc_timestamp)
(userid, movieid, PLAYBACK_STOPPED, movie_pos_in_secs, utc_timestamp)

How are views counted?
How does dashboard show categories?
When a PLAYBACK_STOPPED accompany directly after a PLAYBACK_STARTED
Percentage minutes of movie? Maybe 50 or 90 percent.
*/

CREATE TABLE fact_movie_view (
  date_id int REFERENCES dim_date(id),
  categories_id REFERENCES dim_bridge_categories(id),
  media_id int REFERENCES dim_media(id),
  views int
);

CREATE TABLE dim_bridge_categories (
  id int,
  category_id int
);

CREATE TABLE dim_category (
  id int,
  category text
);

CREATE TABLE dim_date (
  id int,
  date date
);

CREATE TABLE dim_media (
  id int,
  type text,
  name text
);


create table fact_session (
    session_id int primary key,
    date_id int REFERENCES dim_date(id),
    user_id int REFERENCES dim_user(id),
    media_id int REFERENCES dim_media(id),
    play_start_at timestamp,
    play_end_at timestamp,
    session_time double,
)

create table dim_user (
    id primary key,
    first_name text,
    last_name text
    region text
)

-- Average viewer per region
select region, count(*) / count(distinct date_id)
from fact_session s
join dim_user u on u.id = s.user_id
group by u.region

-- Average viewing time
select user_id, sum(session_time) / count(*)
from fact_session s
join dim_user u on u.id = s.user_id
group by user_id

-- source
date_id, user_id, movie_id, total_viewed_secs
date_id, category_id, movie_id, total_viewed

-- https://www.kimballgroup.com/2012/02/design-tip-142-building-bridges/

-- build bridge table from string list column
select unnest(string_to_array(string_list_column, ','))

-- how to catch empty or double loaded data sets?