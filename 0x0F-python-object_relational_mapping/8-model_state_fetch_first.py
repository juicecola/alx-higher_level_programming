#!/usr/bin/python3
""" 8-model_state_fetch_first.py
    prints the first State object from the database.
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name))

    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    Session = session()
    state = Session.query(State).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')


if __name__ == "__main__":
    main()
