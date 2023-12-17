#!/usr/bin/python3
"""
database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306,
                         host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
