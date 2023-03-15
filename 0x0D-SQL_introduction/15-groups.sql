-- Script that lists the number of records with the same score in second_table
SELECT `score`, count(*) as `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
