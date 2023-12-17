#!/usr/bin/python3
"""
Changes and update the name of a State object
from teh database
"""

from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    geaz = sessionmaker(bind=engine)
    session = geaz()

    states = session.query(State).filter(State.id == 2)
    for kete in states:
        kete.name = 'New Mexico'
    session.commit()
    session.close()
