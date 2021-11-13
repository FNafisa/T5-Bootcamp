# SQL 1: Introduction to Databases & Basic SQL Queries

## Sample Lesson Plan
* (90m) [SQL 1 Slides](SQL1_Slides.pdf)
* (15m) [SQLite Setup](sqlite_setup.md)
* (15m) [SQL Joins Preview (Optional)](sql_joins.xlsx)

## Learning Objectives
Students will be able to:

**Introduction to Databases**
* Explain what a database is and the differences between a SQL and NoSQL database
* Explain what a RDBMS is and name a few popular ones
* Explain the differences between data roles such as data engineer and data scientist
* Explain why knowing SQL is important

**Data Models**
* Read a data model and locate the tables, columns, data types, primary keys, and foreign keys
* Recall the various data types, such as INT, TEXT, etc.
* Explain the characteristics of rows in a database, including being unique, unordered, and having one-to-one vs 
one-to-many relationships with other tables

**SQLite Setup**
* Run SQLite on their personal computer and execute a simple `SELECT * FROM names` query in SQLite
* Run DB Browser for SQLite on their personal computer and execute a simple `SELECT * FROM names` query in DB Browser for SQLite
* Explain the benefits of using a database tool like DB Browser for SQLite instead of SQLite directly

**SQL Basics: SELECT, WHERE, ORDER BY, and LIMIT**
* Explain what a SQL query is and how to query data from a single table
* Write a basic SELECT statement
* Write a query that filters data with the WHERE clause
* Write a query that sorts data with the ORDER BY clause
* Write a query that displays a few rows of data with the LIMIT clause

**Aggregations, DISTINCT, and GROUP BY**
* Write a query that aggregates data within the SELECT statement
* Write a query that returns the unique rows of a table
* Write a query that aggregates subsets of data with the GROUP BY clause

**Operators and HAVING**
* List off the different operators within SQL, including arithmetic, comparison, logical and NULL operators
* Write a query that filters aggregated data with the HAVING clause
* Explain the difference between filtering with WHERE and with HAVING

## Additional Resources
[Data Types in SQLite](https://www.sqlite.org/datatype3.html)
[DB Browser for SQLite download](https://sqlitebrowser.org/dl/)