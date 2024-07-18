'''
What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat,
Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can 
override them:
'''

class Vehicle:
    def __init__(self, brand, modal):
        self.brand = brand
        self.modal = modal
    def move(self):
        return "Move!"
    

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        return "Sail!"

class Plane(Vehicle):
    def move(slef):
        return "Fly!"
    
car = Car("TAVA", "V1")
boat = Boat("BOAT", "V2")
plane = Plane("FLIGHT", "V3")

for x in (car, boat, plane):
    print(x.brand, x.modal, x.move())
