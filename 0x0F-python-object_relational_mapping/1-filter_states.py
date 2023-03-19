#!/usr/bin/python3
""" 1-filter_states.py
    lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
