/*
Write a SQL query to find all distinct routes in the Routes table. A route from B to A is considered a duplicate of a route from A to B. You should return the instance that comes first alphabetically based on the Pickup.

Routes table:

+--------+---------+
| Pickup | Dropoff |
+--------+---------+
| A      | B       |
| C      | D       |
| B      | A       |
| C      | D       |
+--------+---------+

For example, your query should return the following for the above table:
+--------+---------+
| Pickup | Dropoff |
+--------+---------+
| A      | B       |
| C      | D       |
+--------+---------+
*/

with tbl_1 as (
select 
    min(Pickup, Dropoff) as p,
    max(Pickup, Dropoff) as d
from Routes
)

select distinct 
    p as Pickup, 
    d as Dropoff
from tbl_1