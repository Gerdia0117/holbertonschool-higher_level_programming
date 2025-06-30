#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query to get cities for the specified state
    # (safe from injection)
    cursor.execute("""SELECT cities.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      WHERE states.name = %s
                      ORDER BY cities.id ASC""", (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Print results as comma-separated city names
    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
