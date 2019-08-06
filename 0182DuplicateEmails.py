# Write your MySQL query statement below
# select Email from
# (
#     select Email, count(Email) as num
#     from Person
#     group by email  
# ) as s
# where num>1
# ;
select Email
from Person
group by email
having count(Email)>1
