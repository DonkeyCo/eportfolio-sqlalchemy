from sqlalchemy import Column, String, Text, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.models.base import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(String(5), primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    salary = Column(Float, nullable=False)

    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=True)

    car = relationship("Car", back_populates="employee", lazy="subquery")
    phone = relationship("Phones")

    # Lazy: n + 1 (size of the result set)
    # Subquery: m + 1 (m - number of relationships)
    # Joined: 1