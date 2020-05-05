from src.models import Employee, Car
import random


emp_data = [
    ("123AB", "Mccarthy", "Tanya", 1205.48),
    ("456CD", "Ryan", "Miriam", 4556.78),
    ("789EF", "Mendoza", "Julie", 1235.45),
    ("123GH", "Richards", "Leona", 9845.21),
    ("456IJ", "Robbins", "Mabel", 3215.98),
    ("789KL", "Malone", "Emelia", 6541.12),
    ("123MN", "Terry", "Sofia", 4875.15),
    ("456OP", "Silva", "Haleema", 5461.65),
    ("789QR", "Thompson", "Francis", 3542.87),
    ("123ST", "Wyatt", "Elin", 2054.65)
]

car_data = [
    ("BMW", "1er"),
    ("BMW", "5er Touring"),
    ("VW", "Golf"),
    ("VW", "Tiguan"),
    ("Mercedes Benz", "S Klasse"),
    ("Mercedes Benz", "CLS"),
    ("smart", "fortwo")
]

def fill(session):
    i = 0
    for emp in emp_data:
        employee = Employee(id=emp[0], name=emp[1], surname=emp[2], salary=emp[3])
        if emp[3] > 3000:
            car = Car(manufacturer=car_data[i][0], model=car_data[i][1])
            employee.car = car
            session.add(car)
            i += 1
        session.add(employee)
    session.commit()