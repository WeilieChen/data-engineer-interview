create table fact_ride (
  id serial primary key,
  rider_id INT references dim_rider(id),
  driver_id INT references dim_driver(id),
  vehicle_id INT references dim_vehicle(id),
  pickup_location_id INT references dim_location(id),
  dropoff_location_id INT references dim_location(id),
  date_id INT references dim_date(id),
  time_day_id INT references dim_time_day(id)
  pickup_ts timestamp,
  dropoff_ts timestamp,
  rate_id int,
  payment_id int,
  charge_amount double
);

create table dim_rider (
  id serial primary key,
  first_name varchar(255),
  last_name varchar(255)
);

create table dim_driver (
  id serial primary key,
  first_name varchar(255),
  last_name varchar(255),
  dob date,
  gender varchar(1),
  license_number varchar(255)
);

create table dim_vehicle (
  id serial primary key,
  make varchar(255),
  model varchar(255),
  "year" int,
  license_plate varchar(255)
);

create table dim_location (
  id serial primary key,
  address varchar(255),
  city varchar(255),
  state varchar(255),
  zip int,
  country varchar(255),
  location_name varchar(255)
  location_type varchar(255)
);

create table dim_payment (
  id serial primary key,
  card_type varchar(255),
  card_number varchar(255),
  expire_date date
);

create table dim_date (
  id serial primary key,
  date date,
  "day" int,
  day_of_week int,
  "month" int,
  "year" int,
  week_id int,
  is_holiday boolean 
)

create table dim_time_day (
  id serial primary key,
  min_number int,
  hour_number int
)

-- All riders that went to airport in the last 24 hours?
select rider_id
from fact_ride r
join dim_location l on l.id = r.dropoff_location_id
join dim_date d on d.id = r.date_id
join dim_time_day td on td.id = r.time_day_id
where date >= (current_timestamp - INTERVAL '24 hour')::date
and hour_number >= date_part(hour, current_timestamp - INTERVAL '24 hour')
and l.location_type = 'AIRPORT'

-- Daily Active Users
select d.date, count(distinct rider_id)
from fact_ride r
join dim_date d on d.id = r.date_id
group by d.date_id

-- Monthly Active Users
select d.month, count(distinct rider_id)
from fact_ride r
join dim_date d on d.id = r.date_id
group by d.month

-- Total Trips Per Week
select d.week_id, count(*)
from fact_ride r
join dim_date d on d.id = r.date_id
group by d.week_id

-- percentage of ridedrs who have only used uber to go to and from airport
drop table if exists fact_ride;
create table fact_ride (
  rider_id int,
  pick_up_id int,
  drop_off_id int
);

drop table if exists dim_rider;
create table if not exists dim_rider (
  id int,
  name text
);

drop table if exists dim_location;
create table if not exists dim_location (
  id int,
  type text
);

insert into fact_ride(rider_id, pick_up_id, drop_off_id)
values 
  (1, 1, 2),
  (1, 2, 1),
  (2, 3, 4);

insert into dim_rider(id, name)
values 
  (1, 'Aaron'),
  (2, 'Bob');

insert into dim_location(id, type)
values 
  (1, 'Airport'),
  (2, 'Restaurant'),
  (3, 'Library'),
  (4, 'Hospital');

with non_airport_rider as (
   select distinct rider_id
   from fact_ride r
   join dim_location pu on pu.id = r.pick_up_id
   join dim_location dof on dof.id = r.drop_off_id
   where pu.type <> 'Airport' and dof.type <> 'Airport'
 )
 select count(distinct case when (pu.type = 'Airport' or dof.type = 'Airport') and rider_id not in (select rider_id from non_airport_rider) then rider_id end) * 1.0 / count(distinct rider_id)
 from fact_ride r
 join dim_location pu on pu.id = r.pick_up_id
 join dim_location dof on dof.id = r.drop_off_id