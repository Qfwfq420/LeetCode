# Write your MySQL query statement below
SELECT a.name as Employee FROM Employee AS a, Employee AS b 
WHERE b.Id = a.managerId and b.salary < a.salary