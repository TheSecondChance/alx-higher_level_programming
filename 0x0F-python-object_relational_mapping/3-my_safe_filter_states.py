#!/usr/bin/python3
"""write one that is safe from MySQL injections"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')

    query = "SELECT * FROM states\
             WHERE states.name = %s\
             ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4], ))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
