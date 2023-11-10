# Write your MySQL query statement below
SELECT email FROM Person AS p
Group by email 
Having Count(email) > 1