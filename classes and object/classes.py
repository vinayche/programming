class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('moves along..')
    def get_make_model(self):
        print(f"I'm a {self.make}  {self.model}.")

my_car1 = Vehicle('Tesla', 'Model 3')   #object1
# print(my_car.make)
# print(my_car.model)
my_car1.get_make_model()
my_car1.moves()   

mycar2 = Vehicle('Cadillac','Escalade')   #object2
mycar2.get_make_model()
mycar2.moves()