import pytest
from calculator import add_num, Car, ElectricCar, Calculator
from apis import get_gas_price, get_power_price

data_to_test = [
        (10,15,0.67),
        (4,2,2),
        (100,50,2)
    ]
@pytest.mark.parametrize(
    'a,b,result', data_to_test
)
def test_add_num(a, b, result):
    res = add_num(a ,b)
    assert  res == result
class TestApi:
    @pytest.mark.parametrize('function', [get_gas_price,get_power_price])
    def test_get_price(self, function):
        res = function()
        assert isinstance(res, int) or  isinstance(res, float)

# fixture
mileages = [1000, 10000]
class TestCar:

    def test_static_year_cost(self, car):
        res = car.static_year_cost()
        assert res == 3700
    @pytest.mark.parametrize('mileage', mileages)
    def test_dynamic_year_cost(self,car, mileage):
        res = car.dynamic_year_cost(mileage)
        expected = car.fuel_economy * mileage / 100 * get_gas_price()
        assert res == expected
    @pytest.mark.parametrize('mileage', mileages)
    def test_year_cost(self,car,mileage):
        res = car.year_cost(mileage)
        expected = car.static_year_cost() + car.dynamic_year_cost(mileage)
        assert res == expected
class TestElectricCar:

    @pytest.mark.parametrize('mileage', mileages)
    def test_dynamic_year_cost(self: int,electrocar,mileage):
        res = electrocar.dynamic_year_cost(mileage)
        expected = electrocar.power_consumption * mileage / 1000 * get_power_price()
        assert res == expected
class TestCalculator:
    def test_add_car(self, calculator, car):
        calculator.add_car(car)
        assert calculator.cars
        assert car in calculator.cars
        assert calculator.cars[car] > 0
    def test_print_cars(self, calculator):
        calculator.print_cars()
    def test_get_left_price(self, calculator,car):
        res = calculator.get_left_price(car)
        assert res
