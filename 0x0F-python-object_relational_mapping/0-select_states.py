#!/usr/bin/python3
"""Get all states"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    namedb = sys.argv[3]
    host = "localhost"
    port = 3306

    db = MySQLdb.connect(host, port, user=username, passwd=password, db=namedb)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = cursor.fetchone()

    while(rows):
        print(rows)
        rows = cursor.fetchone()
