#!/usr/bin/python3
"""
changes the name of a State object
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    gize = sessionmaker(bind=engine)
    session = gize()

    stat = session.query(State).filter(State.id == 2)
    for ket in stat:
        ket.name = 'New Mexico'

    session.commit()
    session.close()
