/* 
0184. https://leetcode.com/problems/department-highest-salary/description/

The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. 
For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

*/

SELECT 
    d.Name AS Department, 
    e.Name AS Employee,
    e.Salary 
FROM Employee e
JOIN (
    SELECT DepartmentId, max(Salary) as max 
    FROM Employee 
    GROUP BY DepartmentId
) m on m.departmentid = e.departmentid
JOIN Department d on d.id = e.DepartmentId
WHERE e.Salary = m.max

SELECT
    department,
    employee,
    salary
FROM (
    SELECT 
        d.Name AS Department, 
        e.Name AS Employee,
        e.Salary,
        dense_rank() over(partition by departmentid order by salary desc) rk
    FROM Employee e
    JOIN Department d on d.id = e.DepartmentId
) a
WHERE rk = 1