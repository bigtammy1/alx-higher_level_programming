#!/usr/bin/python3
"""Script to print states via sqlalchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    result = engine.execute("SELECT * FROM states")
    for row in result:
        print("{}: {}".format(row[0], row[1]))
