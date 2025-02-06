import calculator


if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Toyota Corolla", price=30000, fuel_economy=7, service_cost=1200, insurances_cost=2500)
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 200000,fuel_economy=0, service_cost=0, insurances_cost=5500, power_consumption=150)
    )
    calc.add_car(
        calculator.Car("Range Rover", 650000, 3, service_cost=3000, insurances_cost=7000)
    )
    calc.add_car(
        calculator.Car("Audi", 770000, 3, service_cost=3000, insurances_cost=7000)
    )
    calc.add_car(
        calculator.Car("Zaporozhec", 1090, 3, service_cost=300, insurances_cost=700)
    )
    calc.print_cars()
