#!/usr/bin/python3
"""A script to print all the states and cities """
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).filter(City.state_id == State.id).all()
    for row in result:
        print("{}: ({}) {}".format(row[1].name, row[0].id, row[0].name))
