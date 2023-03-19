#!/usr/bin/python3
""" 13-model_state_delete_a.py
    deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa.
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

    states = Session.query(State).filter(State.name.contains("a"))
    for state in states:
        Session.delete(state)

    Session.commit()

    Session.close()


if __name__ == "__main__":
    main()
