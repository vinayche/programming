class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.model = model  # Public attribute
    
    def display(self):
        return f"{self.make} {self.model}"

car = Car("Toyota", "Camry")
print(car.display())  # Accessing public method
print(car.make)  # Accessing public attribute
