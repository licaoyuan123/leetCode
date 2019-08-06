# Write your MySQL query statement below
select a.Id as 'Id' from weather a join
weather w on DATEDIFF(a.Recorddate, w.Recorddate)=1 and a.Temperature>w.Temperature;
