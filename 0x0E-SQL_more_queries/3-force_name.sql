-- Script that creates the table force_name on your MySQL server.
-- force_name description: id INT, name VARCHAR(256) can’t be null
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not faili-
CREATE TABLE
    IF NOT EXISTS force_name
    (id int, name VARCHAR(256) not NULL);
