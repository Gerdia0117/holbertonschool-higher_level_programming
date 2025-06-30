#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parámetros: usuario, contraseña, base de datos, nombre de estado
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Conexión a la base de datos
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db_name)
    cur = db.cursor()

    # Consulta SQL vulnerable (según las instrucciones): usando format()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
