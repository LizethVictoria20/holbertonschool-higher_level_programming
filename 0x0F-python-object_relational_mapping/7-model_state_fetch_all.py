#!/usr/bin/python3
"""All states via SQLAlchemy"""

from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).all()

    for i in states:
        print("{}: {}".format(i.__dict__['id'], i.__dict__['name']))
