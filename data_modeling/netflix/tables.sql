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
playback_segments = (userid, movieid, pb_start_pos, pb_end_pos, pb_start_timestamp, pb_end_timestamp)