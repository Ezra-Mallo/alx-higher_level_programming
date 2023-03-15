-- Script that lists all records of the second_table where name != blank
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != NULL
ORDER BY `score` DESC;
