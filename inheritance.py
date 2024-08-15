class Vehicle:                       #class 
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

class Airplane(Vehicle):
    def moves(self):
        print("Fling along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class Golfcart(Vehicle):
    pass

cessna = Airplane('Cessna','Skyhawk')
mack = Truck('Mack','Pinnacle')
golfwagon = Golfcart('Yamaha','GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()