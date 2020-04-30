from sqlalchemy import Column, Float, String, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.models.base import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(String(5), primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    salary = Column(Float)

    # One-to-One relationship with Car - 1 Employee has 1 Car and vice versa
    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=True)

    car = relationship("Car", uselist=False, back_populates="employee", lazy="selectin")
