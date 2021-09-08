/* 
Write a SQL query to return:
1. The number of people in the IT department who have a salary greater than 70000
2. The number of people in the Sales department who have a salary greater than 50000

Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+-------+
| Id | Name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+



For example, your query should return the following for the above table:
+------------+-------+
| Department | Count |
+------------+-------+
| IT         | 3     |
| Sales      | 2     |
+------------+-------+ 
*/
with stage as (
    select d.name as department, e.id as employee_id
    from employee e
    join department d on d.id = e.departmentid
    where d.name = 'IT' and e.salary > 70000

    union all

    select d.name as department, e.id as employee_id
    from employee e
    join department d on d.id = e.departmentid
    where d.name = 'Sales' and e.salary > 50000
)
select department, count(employee_id)
from stage
group by department;

select 
    Department,
    sum(cnt) as Count
from (select 
        b.Name as Department,
        case
            when b.Name = 'IT' and a.Salary > 70000
            then 1
            when b.Name = 'Sales' and a.Salary > 50000
            then 1
            else 0
        end as cnt
    from Employee a
    inner join Department b
         on a.DepartmentId = b.Department) a
group by Department;

select d.name as department, 
    sum(case
            when d.name = 'IT' and e.salary > 70000 then 1
            when d.name = 'Sales' and e.salary > 50000 then 1
            else 0
        end) as count
from employee e
join department d on d.id = e.departmentid
group by department;