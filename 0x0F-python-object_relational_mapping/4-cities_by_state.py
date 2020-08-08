#!/usr/bin/python3
"""Cities by states"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    namedb = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=namedb)

    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id""")
    rows = cursor.fetchone()

    while(rows):
        print(rows)
        rows = cursor.fetchone()
