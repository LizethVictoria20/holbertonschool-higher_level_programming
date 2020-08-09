#!/usr/bin/python3
"""Cities in state"""

from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State, City).join(City).all()

    for i in states:
        print("{}: {} {}".format(
            i[0].__dict__['name'],
            i[1].__dict__['id'],
            i[1].__dict__['name']))
