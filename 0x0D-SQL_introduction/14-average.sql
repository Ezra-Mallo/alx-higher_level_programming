-- Script that removes all records with a score <= 5 in second_table
SELECT AVG(`score`) as `average` FROM `second_table`
