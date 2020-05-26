from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.utils import db

from src.models import Base, Car, Employee

print("Hello World")


engine = create_engine('sqlite:///eport.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees = session.query(Employee).filter(Employee.salary >= 4000)
print("-------------------")
[print(e.car.manufacturer) for e in employees]