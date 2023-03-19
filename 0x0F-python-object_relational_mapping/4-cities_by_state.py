#!/usr/bin/python3
""" 4-cities_by_state.py
    lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        "localhost",
        mysql_username,
        mysql_password,
        database_name,
        3306)

    cursor = db.cursor()
    cursor.execute(
        ("SELECT cities.id, cities.name, states.name FROM cities "
         "LEFT JOIN states ON cities.state_id = states.id "
         "ORDER BY cities.id ASC;"))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
