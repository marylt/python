'''
Name: Mary Ton
StudentDirectory ID: mton
Date: 2019-10-11
Assignment: Module 6 Lab Worksheet
'''
class Pizza():

    def __init__(self):
        self.toppings = []
    def add_topping(self, topping):
        if len(self.toppings) < 7:
            self.toppings.append(topping)
        else:
            print('Too many toppings!')

class Topping():

    def __init__(self, name, num_pieces):
        self.name = name
        self.num_pieces = num_pieces
    def __repr__(self):
        return "{} pieces of {}".format(self.num_pieces, self.name)

mypizza = Pizza()
mytopping = Topping('pepperoni', 10)
mypizza.add_topping(mytopping)
for i in range (7):
    print(mypizza)
    mypizza.add_topping(Topping('mushrooms', 15))

print(mypizza)
print(mytopping)
print(mypizza.toppings)
