#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    mesak = sessionmaker(bind=engine)
    session = mesak()

    stat = State(name='Louisiana')
    session.add(stat)
    session.commit()
    print(stat.id)
    session.close()
