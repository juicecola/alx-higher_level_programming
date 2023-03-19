#!/usr/bin/python3
""" 11-model_state_insert.py
    Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
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

    state = State(name="Louisiana")

    Session.add(state)
    Session.commit()

    print(state.id)

    Session.close()


if __name__ == "__main__":
    main()
