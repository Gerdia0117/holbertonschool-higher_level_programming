#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query and delete all State objects that contain the letter 'a'
    states_to_delete = session.query(State).filter(
        State.name.contains('a')).all()

    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
