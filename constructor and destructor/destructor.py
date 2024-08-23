class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"{self.make} {self.model} created.")

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def __del__(self):
        print(f"{self.make} {self.model} destroyed.")

# Creating an object of the Car class
car = Car("Toyota", "Camry", 2022)
print(car.display_info())  # Output: 2022 Toyota Camry

# Deleting the object explicitly (optional)
del car  # This will call the destructor
