#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    giaz = sessionmaker(bind=engine)

    session = giaz()

    keat = session.query(State).filter(State.name.contains('a')).all()

    for state in keat:
        session.delete(state)

    session.commit()
    session.close()
