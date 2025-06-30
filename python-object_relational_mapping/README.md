# Python Object Relational Mapping Project

![ORM Diagram](https://i.imgur.com/JK9yX2C.png)

This project explores the connection between Python and databases using both raw SQL queries (MySQLdb) and Object Relational Mapping (SQLAlchemy).

## Table of Contents
1. [Background](#background)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Project Tasks](#project-tasks)
6. [Usage Examples](#usage-examples)
7. [Resources](#resources)

## Background

This project bridges two worlds:
1. **MySQLdb**: Direct SQL queries from Python
2. **SQLAlchemy**: ORM that abstracts database operations

Key difference:
```python
# Without ORM (MySQLdb)
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# With ORM (SQLAlchemy)
session.query(State).order_by(State.id).all()

Learning Objectives

After completing this project, you should be able to:

✔ Connect Python to MySQL databases
✔ Execute SQL queries from Python scripts
✔ Understand ORM concepts and benefits
✔ Map Python classes to database tables
✔ Perform CRUD operations using SQLAlchemy
✔ Handle database relationships in Python
Requirements

    Python 3.8.5 on Ubuntu 20.04 LTS

    MySQLdb version 2.0.x

    SQLAlchemy version 1.4.x

    File requirements:

        First line: #!/usr/bin/python3

        Executable permissions

        PEP 8 compliant (pycodestyle)

        Comprehensive documentation

Installation
1. Install MySQL Server
bash

sudo apt update
sudo apt install mysql-server
mysql --version  # Verify 8.0.x

2. Install MySQLdb
bash

sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient
python3 -c "import MySQLdb; print(MySQLdb.version_info)"  # Verify 2.0.x

3. Install SQLAlchemy
bash

sudo pip3 install SQLAlchemy
python3 -c "import sqlalchemy; print(sqlalchemy.__version__)"  # Verify 1.4.x

Project Tasks
MySQLdb Tasks (Raw SQL)
Task	File	Description
0	0-select_states.py	List all states
1	1-filter_states.py	Filter states starting with 'N'
2-3	2-3-my*.py	Safe state filtering (SQL injection proof)
4-5	4-5-*.py	City/state relationships
SQLAlchemy Tasks (ORM)
Task	File	Key Concept
6	model_state.py	Define State model
7-9	7-9-*.py	Query State objects
10-13	10-13-*.py	Advanced ORM operations
14	model_city.py	City model with relationships
Usage Examples
MySQLdb Example
bash

./0-select_states.py root root hbtn_0e_0_usa
# Output: (1, 'California'), (2, 'Arizona')...

SQLAlchemy Example
bash

./7-model_state_fetch_all.py root root hbtn_0e_6_usa
# Output: 1: California, 2: Arizona...

Creating Models
python

# model_state.py
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

Resources
Essential Reading

    MySQLdb Documentation

    SQLAlchemy Tutorial

    Python ORM Concepts

Advanced Topics

    SQLAlchemy Session Basics

    Database Relationships in ORM
