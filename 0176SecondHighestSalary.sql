# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary
from Employee
where Salary< (Select max(Salary) from Employee);
