#!/usr/bin/python3
""" 12-model_state_update_id_2.py
    changes the name of a State object from the database hbtn_0e_6_usa.
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

    state = Session.query(State).get(2)
    state.name = "New Mexico"
    Session.commit()

    Session.close()


if __name__ == "__main__":
    main()
