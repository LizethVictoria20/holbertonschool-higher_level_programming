#!/usr/bin/python3
"""Get a state"""

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
    nameState = sys.argv[4]

    aux = ""

    for i in states:
        if nameState in i.__dict__['name']:
            aux = i.__dict__['id']

    if aux != "":
        print(aux)
    else:
        print("Not found")
