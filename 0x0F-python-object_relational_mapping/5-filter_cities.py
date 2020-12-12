#!/usr/bin/python3
"""Cities by states..."""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    namedb = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=namedb)

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id AND states.name = "{:s}"
    ORDER BY cities.id ASC""".format(stateName))

    rows = cursor.fetchone()
    rowState = []

    while(rows):
        rowState.append(rows[0])
        rows = cursor.fetchone()
    print(', '.join(rowState))
