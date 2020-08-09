#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    namedb = sys.argv[3]
    nameSearched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=namedb)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE states.name LIKE BINARY "{:s}"
    ORDER BY states.id ASC""".format(nameSearched))

    emptyList = cursor.fetchall()

    for i in emptyList:
        print(i)
