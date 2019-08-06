CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M int;
set M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select DISTINCT Salary from Employee Order by Salary desc limit M, 1
      
  );
END
