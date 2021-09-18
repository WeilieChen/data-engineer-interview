/* 
Several friends at a cinema ticket office would like to reserve consecutive available seats.
Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?

+---------+------+ 
| seat_id | free |
+---------+------+
| 1	      | 1    |
| 2	      | 0    |
| 3	      | 1    |
| 4	      | 1    |  
| 5	      | 1    |
+---------+------+

Your query should return the following result for the sample case above.

+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+
*/

select s1.seat_id
from seats s1
left join seats s2 on s1.seat_id = s2.seat_id - 1 and s2.free = 1
where s1.free = 1
and s2.seat_id is not null
