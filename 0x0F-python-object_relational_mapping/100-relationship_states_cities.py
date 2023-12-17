#!/usr/bin/python3
'''
creates the State “California”
with the City class “San Francisco”
'''


from sys import argv
from sqlalchemy import create_engine
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    geaz = sessionmaker(bind=engine)
    session = geaz()

    ket = State(name='California')
    kete = City(name='San Francisco', state=ket)
    session.add(kete)
    session.commit()

    session.close()
