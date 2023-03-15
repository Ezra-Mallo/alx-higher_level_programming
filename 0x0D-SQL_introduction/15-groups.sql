-- Script that removes all records with a score <= 5 in second_table
select `score`, count(*) as `number`
from `second_table`
group by `score`
order by `score` DESC;
