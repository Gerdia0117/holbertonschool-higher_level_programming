# Python - Object-relational mapping

This project explores the connection between Python and MySQL databases using two approaches:
- Direct database queries using MySQLdb
- Object Relational Mapping (ORM) using SQLAlchemy

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- pycodestyle version 2.7.*

## Installation

```bash
# Install MySQL 8.0
sudo apt update
sudo apt install mysql-server

# Install MySQLdb module
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient==2.0.3

# Install SQLAlchemy module
sudo pip3 install SQLAlchemy==1.4.22
```

## Files

- `0-select_states.py` - Lists all states from the database
- `1-filter_states.py` - Lists all states with name starting with N
- `2-my_filter_states.py` - Displays values matching user input (unsafe)
- `3-my_safe_filter_states.py` - Displays values matching user input (SQL injection safe)
- `4-cities_by_state.py` - Lists all cities from the database
- `5-filter_cities.py` - Lists all cities of a specific state
- `model_state.py` - Contains the State class definition
- `6-model_state.py` - Creates states table using SQLAlchemy
- `7-model_state_fetch_all.py` - Lists all State objects
- `8-model_state_fetch_first.py` - Prints the first State object
- `9-model_state_filter_a.py` - Lists State objects containing letter 'a'
- `10-model_state_my_get.py` - Prints State object with given name
- `11-model_state_insert.py` - Adds State object "Louisiana"
- `12-model_state_update_id_2.py` - Changes name of State with id=2
- `13-model_state_delete_a.py` - Deletes State objects containing letter 'a'
- `model_city.py` - Contains the City class definition
- `14-model_city_fetch_by_state.py` - Prints all City objects

## Author

Holberton School Project
