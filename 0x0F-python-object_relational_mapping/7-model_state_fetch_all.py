#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    wek = sessionmaker(bind=engine)
    session = wek()

    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
    session.close()