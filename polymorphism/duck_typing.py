class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class Bird:
    def speak(self):
        return "Chirp"

# A function that uses polymorphism through duck typing
def make_animal_speak(animal):
    return animal.speak()

# Different types of animals, but they can all "speak"
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(make_animal_speak(animal))
