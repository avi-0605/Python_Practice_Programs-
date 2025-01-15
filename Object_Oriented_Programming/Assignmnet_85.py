#Class Car **and Inheritance Create a base class Car with attributes: make, model, year. Create a derived class ElectricCar with an additional battery_size attribute.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        return f"{super().display_info()}, Battery: {self.battery_size} kWh"


car = Car("Toyota", "Camry", 2020)
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

print(car.display_info())        
print(electric_car.display_info())  