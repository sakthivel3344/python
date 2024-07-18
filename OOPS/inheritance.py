class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

p = Person("Spider", "Man")

p.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname) # or
        super().__init__(fname, lname)
        self.graduationYear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "of the class of", self.graduationYear)

s = Student("Peter", "Parker", 2024)
s.printname()
s.welcome()