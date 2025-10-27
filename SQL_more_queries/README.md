# SQL - More queries

This project focuses on advanced MySQL queries including user management, privileges, constraints, joins, and subqueries.

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements

- All files executed on Ubuntu 20.04 LTS using MySQL 8.0
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)

## Tasks

0. **0-privileges.sql** - Lists all privileges of MySQL users user_0d_1 and user_0d_2
1. **1-create_user.sql** - Creates the MySQL server user user_0d_1
2. **2-create_read_user.sql** - Creates the database hbtn_0d_2 and user user_0d_2
3. **3-force_name.sql** - Creates the table force_name with NOT NULL constraint
4. **4-never_empty.sql** - Creates the table id_not_null with default value
5. **5-unique_id.sql** - Creates the table unique_id with UNIQUE constraint
6. **6-states.sql** - Creates database hbtn_0d_usa and table states with PRIMARY KEY
7. **7-cities.sql** - Creates table cities with FOREIGN KEY
8. **8-cities_of_california_subquery.sql** - Lists all cities of California using subquery
9. **9-cities_by_state_join.sql** - Lists all cities with their states using JOIN
10. **10-genre_id_by_show.sql** - Lists shows with at least one genre
11. **11-genre_id_all_shows.sql** - Lists all shows including those without genres
12. **12-no_genre.sql** - Lists shows without a genre
13. **13-count_shows_by_genre.sql** - Lists genres with count of shows
14. **14-my_genres.sql** - Lists all genres of the show Dexter
15. **15-comedy_only.sql** - Lists all Comedy shows
16. **16-shows_by_genre.sql** - Lists all shows and their genres
