-- accepted values
with all_values as (

    select
        data_type_id as value_field,
        count(*) as n_records

    from silver_limeade_platform.activity_measurements
    group by 1

)

select *
from all_values
where value_field not in (
    '0','1','2'
)

-- relationship check
with child as (
    select challenge_id as from_field
    from silver_limeade_platform.activity_comments
    where challenge_id is not null
),

parent as (
    select challenge_id as to_field
    from silver_limeade_platform.challenges
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null

-- column is unique
select
    row_uuid as unique_field,
    count(*) as n_records

from silver_limeade_platform.account_statuses
where row_uuid is not null
group by row_uuid
having count(*) > 1


-- rolling avg
select
  date,
  value,
  avg(value) 
    over (order by date asc
          rows between 6 preceding and current row) as avg,
from signups
order by 1 desc

select signups.date, signups.count, avg(signups_past.count)
from signups
join signups as signups_past 
  on signups_past.date 
     between dateadd(day, -6, signups.date) and signups.date
group by signups.date, signups.count

-- duplicates
  SELECT
    email_address,
    date_of_birth,
    COUNT(*)
  FROM customers
  GROUP BY email_address, date_of_birth
  HAVING COUNT(*) >= 2

  SELECT
  email_address,
  date_of_birth,
  MAX(customer_first_name) AS customer_first_name,
  MAX(customer_last_name) AS customer_last_name
FROM customers
GROUP BY email_address, date_of_birth

-- optiziming slow running queries
-- Table scans — Where the DB is reading every single entry of a table, generating lots of disk use (which is slow)
-- High cardinality operations — Whether there’s an index being used or not, when the DB has to work with a large amount of rows, it again means more disk and memory use and just takes time to go through all that
-- Loop-like operations over large numbers of records— Things like correlated subqueries where the DB has to do a separate subquery for a bunch of rows, much like a for-loop in general programming.
-- Writing to disk due to memory constraints —You find this both in RDBMS and Hadoop systems, when something becomes too big to fit in memory to process, it has to write down its work to disk to continue without crashing
-- Using the network — especially true for distributed systems where network traffic is almost required, it makes disks look fast in comparison.

-- max without using max()
SELECT DISTINCT t1.col
FROM tableName t1
  LEFT JOIN tableName t2
    ON t2.col > t1.col AND t2.col IS NOT NULL
WHERE t2.col IS NULL

-- get max and second max, without using max()
SELECT t1.col
FROM tableName t1
  LEFT JOIN tableName t2
    ON t2.col > t1.col AND t2.col IS NOT NULL
group by t1.col
having count(t2.col) in (0, 1)