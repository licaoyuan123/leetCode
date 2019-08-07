# Write your MySQL query statement below

select Score, (select  count(distinct Score) from Scores where Score>=s.Score) Rank
from Scores as s
order by Rank asc


 
