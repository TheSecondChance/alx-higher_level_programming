#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    tya = "SELECT * FROM states\
             WHERE states.name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(sys.argv[4])
    cursor = db.cursor()
    cursor.execute(tya)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
