class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
    
    def __display(self):  # Private method
        return f"{self.__make} {self.__model}"
    
    def get_details(self):
        return self.__display()  # Accessing private method within the class

car = Car("Toyota", "Camry")
# print(car.__make)  # This would raise an AttributeError
print(car.get_details())  # This works because it's accessed through a public method
