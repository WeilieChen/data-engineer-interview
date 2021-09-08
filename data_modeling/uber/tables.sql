create table fact_ride (
  id serial primary key,
  rider_id INT references dim_rider(id),
  driver_id INT references dim_driver(id),
  vehicle_id INT references dim_vehicle(id),
  pickup_location_id INT references dim_location(id),
  dropoff_location_id INT references dim_location(id),
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
  year int,
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
);

create table dim_payment (
  id serial primary key,
  card_type varchar(255),
  card_number varchar(255),
  expire_date date
);