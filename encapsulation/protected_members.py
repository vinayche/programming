class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
    
    def display(self):
        return f"{self._make} {self._model}"

class SportsCar(Car):
    def __init__(self, make, model, top_speed):
        super().__init__(make, model)
        self._top_speed = top_speed  # Additional protected attribute
    
    def display(self):
        return f"{self._make} {self._model} with top speed {self._top_speed} mph"

car = SportsCar("Ferrari", "488", 211)
print(car.display())  # Accessing protected members through subclass
