<h1 align="center"> ALX Projects</h1>
<h1 align="center"> 0x0D. SQL - Introduction </h1>
<p align ="center">
<img src="https://github.com/Ezra-Mallo/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/images/mySQL.jpg"
alt="mySQL">
</p>
<p>
<img src="https://github.com/Ezra-Mallo/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/images/MySQL.jpg"
alt="MySQL">
</p>

## Resources to read or watch:
* [What is Database & SQL?](https://intranet.alxswe.com/rltoken/yyRKTEdRkYEVlRgZPbasjw)
* [A Basic MySQL Tutorial](https://intranet.alxswe.com/rltoken/sV2PtK5YfQsXWW1malRZ5Q)
* [Basic SQL statements: DDL and DML -no need to read the chapter “Privileges”](https://intranet.alxswe.com/rltoken/IUKo4-UaRZSKPvXr5u9oBw)
* [Basic queries: SQL and RA](https://intranet.alxswe.com/rltoken/rXKvu2u7vg1Hj6bnX7UgMg)
* [SQL technique: functions](https://intranet.alxswe.com/rltoken/-Riv_dzSYsJyvy-LlaO6Mg)
* [SQL technique: subqueries](https://intranet.alxswe.com/rltoken/QpIXoR--8eBIaidgSWYsBQ)
* [What makes the big difference between a backtick and an apostrophe?](https://intranet.alxswe.com/rltoken/Gt0nFJPJRwW2Y0izzwbVrw)
* [MySQL Cheat Sheet](https://intranet.alxswe.com/rltoken/1oU1LwCksQLXjs6fZYezrw)
* [MySQL 8.0 SQL Statement Syntax](https://intranet.alxswe.com/rltoken/HmdmLiYBM0Q34iCYPWd9XQ)
* [installing MySQL in Ubuntu 20.04](https://intranet.alxswe.com/rltoken/IpYI9rgbwfjxOAQQgpHCmQ)

* [Databases](https://intranet.alxswe.com/concepts/37)
* [Databases](https://intranet.alxswe.com/concepts/556)
## More Info
### Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$


## Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$


### Connect to your MySQL server:
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$


## Use “container-on-demand” to run MySQL
###In the container, credentials are root/root
* Ask for container Ubuntu 20.04
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:

$ service mysql start
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$

###In the container, credentials are root/root




