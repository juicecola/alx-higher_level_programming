#!/usr/bin/python3
""" 14-model_city_fetch_by_state.py
    that prints all City objects from the database hbtn_0e_14_usa.
"""

from model_state import Base, State
from model_city import City
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

    for state, city in session.query(State, City).filter(
            City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    Session.close()


if __name__ == "__main__":
    main()
