#!/usr/bin/python3
"""Filter states..."""

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
    cursor.execute("""SELECT * FROM states WHERE states.name
    LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = cursor.fetchone()

    while(rows):
        print(rows)
        rows = cursor.fetchone()
