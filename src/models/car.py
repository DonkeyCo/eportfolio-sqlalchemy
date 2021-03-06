from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from src.models.base import Base

class Car(Base):
    __tablename__ = "car"

    car_id = Column(Integer, primary_key=True, nullable=False)
    manufacturer = Column(Text, nullable=False)
    model = Column(Text, nullable=False)

    employee = relationship("Employee", uselist=False, back_populates="car")
    
