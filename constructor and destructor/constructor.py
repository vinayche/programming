class Car:
    def __init__(self, make, model, year):
        self.make = make  # Instance variable
        self.model = model  # Instance variable
        self.year = year  # Instance variable

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object of the Car class
car = Car("Toyota", "Camry", 2022)
print(car.display_info())  # Output: 2022 Toyota Camry
