# название файла фиксированное, файл предназначен для размещенния fixture
import pytest
from calculator import Car, ElectricCar, Calculator
@pytest.fixture(scope='session')
def car():
        return Car("Toyota Corolla", price=30000,
                   fuel_economy=7, service_cost=1200, insurances_cost=2500)
@pytest.fixture()
def electrocar():
        return ElectricCar("Tesla Model 3", 200000,fuel_economy=0, service_cost=0,
                           insurances_cost=5500, power_consumption=150)

@pytest.fixture(scope='session')
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return