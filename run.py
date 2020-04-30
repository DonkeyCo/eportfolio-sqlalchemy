from src.models import Car, Employee, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

from src.utils import db


# Create engine
engine = create_engine('sqlite:///eport.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees = session.query(Employee).filter(Employee.salary >= 4000).all()

# db.fill(session)
print("--------------------------")
# [print(e.name) for e in employees]
[print(e.car.model) for e in employees]
