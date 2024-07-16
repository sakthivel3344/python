class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name # returning a value for p1 when it gets printed
    
    def talk(self):
        return "Talking"

p1 = Person("Sakthivel", 21) # object for class created

print(p1)
print(p1.name, p1.age, p1.talk())