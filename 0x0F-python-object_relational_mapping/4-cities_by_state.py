#!/usr/bin/python3
"""
lists all cities from the database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')

    tyak = "SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states\
             WHERE cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(tyak)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
