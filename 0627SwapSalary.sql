# Write your MySQL query statement below
update salary
set sex=CASE sex
when 'm' Then 'f'
else 'm'
end;
