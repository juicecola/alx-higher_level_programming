#!/usr/bin/python3
""" 5-filter_cities.py
    takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(
        "localhost",
        mysql_username,
        mysql_password,
        database_name,
        3306)

    cursor = db.cursor()
    cursor.execute(
        ("SELECT cities.id, cities.name, states.name FROM "
         "cities LEFT JOIN states ON cities.state_id = states.id WHERE "
         "states.name = %s ORDER BY cities.id ASC"), (search, ))

    print(", ".join([row[1] for row in cursor.fetchall()]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
