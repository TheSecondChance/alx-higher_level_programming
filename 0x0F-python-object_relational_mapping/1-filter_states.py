#!/usr/bin/python3
"""
all states with a name starting
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')

    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY 'N%'\
             ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
