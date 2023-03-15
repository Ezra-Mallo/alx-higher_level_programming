-- Script that lists all records of the second_table where name != blank

hat lists the number of records with the same score in second_table
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != NULL
ORDER BY `score` DESC;
