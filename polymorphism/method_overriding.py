class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
