-- Script that removes all records with a score <= 5 in second_table
SELECT `score`, count(*) as `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
