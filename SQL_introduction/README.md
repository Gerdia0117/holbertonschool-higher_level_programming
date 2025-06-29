# MySQL Database Project

![MySQL Database](https://www.mysql.com/common/logos/logo-mysql-170x115.png)

## Table of Contents
1. [Project Description](#project-description)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Installation Guide](#installation-guide)
5. [Task Solutions](#task-solutions)
6. [Usage Examples](#usage-examples)
7. [SQL Best Practices](#sql-best-practices)
8. [Resources](#resources)

## Project Description

This project introduces fundamental MySQL database concepts through 16 practical SQL script exercises, covering:

- Database creation and management
- Table structure definition
- Basic CRUD operations (Create, Read, Update, Delete)
- Data querying and filtering
- Aggregation functions

## Learning Objectives

After completing this project, you'll understand:

✔ Database fundamentals and relational databases
✔ SQL syntax and MySQL specifics
✔ Database/table creation and modification
✔ Data manipulation (INSERT, UPDATE, DELETE)
✔ Advanced query techniques including subqueries and functions

## Requirements

- **Environment**: Ubuntu 20.04 LTS with MySQL 8.0.25
- **Script Requirements**:
  - All files must end with a new line
  - SQL queries must have descriptive comments
  - SQL keywords must be uppercase (SELECT, WHERE, etc.)
  - First line of each file must describe the task

## Installation Guide

### For Ubuntu 22.04 (Current image on CoD Platform):

```bash
# Update package list
apt update

# Install mysql-server package
apt install -y mysql-server

# Check installation
mysql --version
# Should return: mysql Ver 8.0.39-0ubuntu0.22.04.1

# Start MySQL service
service mysql start

# Connect to MySQL
mysql -uroot

For Ubuntu 20.04 Sandbox:
bash

# Start MySQL service
service mysql start

# Connect (credentials are root/root)
mysql -uroot -p

Task Solutions
Basic Database Operations
Task	File	Description	Solution
0	0-list_databases.sql	Lists all databases	SHOW DATABASES;
1	1-create_database_if_missing.sql	Creates database if not exists	CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
2	2-remove_database.sql	Deletes database	DROP DATABASE IF EXISTS hbtn_0c_0;
Table Operations
Task	File	Description	Solution
3	3-list_tables.sql	Lists tables in a database	SHOW TABLES;
4	4-first_table.sql	Creates basic table	CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
5	5-full_table.sql	Shows table structure	SHOW CREATE TABLE first_table;
Data Manipulation
Task	File	Description	Solution
6	6-list_values.sql	Lists all table rows	SELECT * FROM first_table;
7	7-insert_value.sql	Inserts new record	INSERT INTO first_table (id, name) VALUES (89, 'Best School');
8	8-count_89.sql	Counts specific records	SELECT COUNT(*) FROM first_table WHERE id = 89;
Usage Examples

1. List all databases:
bash

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

2. Create and populate a table:
bash

# Create database
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p

# Create table
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# Insert data
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# View data
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

3. Advanced queries:
bash

# Get average score
cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# Group by score
cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SQL Best Practices

    Always include comments:

sql

-- Lists all students in Batch 3 (the best batch!)
SELECT id, name FROM students WHERE batch_id = 3;

    Use consistent formatting:

sql

SELECT
    s.id,
    s.name,
    COUNT(r.id) AS review_count
FROM
    students s
LEFT JOIN
    reviews r ON s.id = r.student_id
WHERE
    s.batch_id = 3
GROUP BY
    s.id
ORDER BY
    review_count DESC;

    Handle errors gracefully:

sql

-- Creates table only if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

Resources

    MySQL 8.0 Documentation

    MySQL Tutorial

    SQL Style Guide

    Ubuntu MySQL Installation

Project Status: Complete
MySQL Version: 8.0.25
Author: [Your Name]
Institution: Holberton School
Last Updated: June 2023
