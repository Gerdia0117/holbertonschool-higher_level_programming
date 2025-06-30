# SQL More Queries Project

![MySQL Logo](https://www.mysql.com/common/logos/logo-mysql-170x115.png)

This project builds on basic MySQL knowledge to explore more advanced query techniques, user management, and database constraints.

## Table of Contents
1. [Resources](#resources)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Project Tasks](#project-tasks)
6. [Usage Examples](#usage-examples)
7. [SQL Best Practices](#sql-best-practices)

## Resources

### Essential Reading
- [MySQL User Creation & Permissions](https://dev.mysql.com/doc/refman/8.0/en/creating-accounts.html)
- [MySQL GRANT Statement](https://dev.mysql.com/doc/refman/8.0/en/grant.html)
- [MySQL Constraints](https://dev.mysql.com/doc/refman/8.0/en/constraints.html)
- [SQL Joins Explained](https://www.w3schools.com/sql/sql_join.asp)

### Advanced Techniques
- [Multiple Joins and DISTINCT](https://www.mysqltutorial.org/sql-distinct.aspx)
- [Join Types](https://www.sqlshack.com/sql-multiple-join/)
- [Subqueries](https://www.mysqltutorial.org/mysql-subquery/)
- [UNION and MINUS](https://www.mysqltutorial.org/sql-union-mysql.aspx)

### Reference Materials
- [MySQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [Seven Types of SQL Joins](https://www.sqlshack.com/learn-sql-types-of-joins/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Learning Objectives

After completing this project, you should be able to:

✔ Create and manage MySQL users and privileges
✔ Implement PRIMARY KEY and FOREIGN KEY constraints
✔ Use NOT NULL and UNIQUE constraints effectively
✔ Retrieve data from multiple tables using joins
✔ Write subqueries and understand their use cases
✔ Differentiate between JOIN and UNION operations

## Requirements

- **Environment**: Ubuntu 20.04 LTS with MySQL 8.0.25
- **File Standards**:
  - All files must end with a newline
  - Each SQL query must have a descriptive comment above it
  - Files must start with a comment describing the task
  - SQL keywords must be uppercase (SELECT, WHERE, etc.)
- **Mandatory**: README.md at project root

## Installation

### For Ubuntu 20.04:

```bash
# Update package list
sudo apt update

# Install MySQL Server
sudo apt install mysql-server

# Verify installation
mysql --version
# Should return: mysql  Ver 8.0.25-0ubuntu0.20.04.1

# Start MySQL service
service mysql start

# Connect to MySQL (password: root)
mysql -uroot -p

For Sandbox Environment:
bash

# Start MySQL service
service mysql start

# Connect (credentials are root/root)
mysql -uroot -p

Project Tasks
User Management
Task	File	Description	Solution Example
0	0-privileges.sql	List user privileges	SHOW GRANTS FOR 'user_0d_1'@'localhost';
1	1-create_user.sql	Create admin user	CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
2	2-create_read_user.sql	Create read-only user	GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
Table Constraints
Task	File	Description	Key Feature
3	3-force_name.sql	NOT NULL constraint	name VARCHAR(256) NOT NULL
4	4-never_empty.sql	DEFAULT constraint	id INT DEFAULT 1
5	5-unique_id.sql	UNIQUE constraint	id INT DEFAULT 1 UNIQUE
Database Design
Task	File	Description	Key Feature
6	6-states.sql	Primary key	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
7	7-cities.sql	Foreign key	FOREIGN KEY (state_id) REFERENCES states(id)
Usage Examples

1. Create a database and user:
bash

cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p

2. Import a database dump:
bash

curl "https://example.com/dump.sql" -s | mysql -uroot -p hbtn_0d_tvshows

3. Run a complex query:
bash

cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SQL Best Practices

    Consistent Formatting:

sql

-- Retrieve shows with their genres
SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
    tv_shows.title ASC,
    tv_genres.name ASC;

    Proper Constraints:

sql

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

    Secure User Creation:

sql

-- Create user with specific privileges
CREATE USER IF NOT EXISTS 'read_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT SELECT ON database.* TO 'read_user'@'localhost';
FLUSH PRIVILEGES;
