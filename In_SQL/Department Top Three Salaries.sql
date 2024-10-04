# Write your MySQL query statement below

SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary 
FROM Department d JOIN Employee e1 ON d.id = e1.departmentId 
WHERE 3 > (SELECT COUNT(DISTINCT e2.salary) FROM Employee e2 WHERE e2.salary > e1.salary AND e2.departmentId = e1.departmentId)