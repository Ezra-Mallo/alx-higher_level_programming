<h1 align="center"> 0x0F. Python - Object-relational mapping  </h1>
<p align ="center">
<img src="https://github.com/Ezra-Mallo/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/images/SQLAlchemy.png"
alt="SQLAlchemy">
</p>
<p>
<img src="https://github.com/Ezra-Mallo/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/images/MySQL.jpg"
alt="MySQL">
</p>




## Python | OOP | SQL | MySQL | ORM | SQLAlchemy

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.


###How to run the sql
    $ cat <sql_file_name.sql> | sudo mysql -uroot -p
        example: to execute the sql script in "0-select_stgate.sql"
            $ cat 0-select_states.sql | mysql -uroot -p

###How to run the orm file
    $ ./<python_orm_file_name.py> root root <database_name> 
        example: to execute the sql script in "0-select_stgate.sql"
            $ ./0-select_states.py root root hbtn_0e_0_usa


## Resources read or watch:

* [Object-relational mappers]()
* [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)]()
* [MySQLdb tutorial]()
* [SQLAlchemy tutorial]()
* [SQLAlchemy]()
* [mysqlclient/MySQLdb]()
* [Introduction to SQLAlchemy]()
* [Flask SQLAlchemy]()
* [10 common stumbling blocks for SQLAlchemy newbies]()
* [Python SQLAlchemy Cheatsheet]()
* [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)]()
* [SQLAlchemy Tutorial]()