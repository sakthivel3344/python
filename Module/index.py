import moduleone as firstModule
import person
from person import persondata

firstModule.sayHello()
firstModule.sayBye()

person.printPersonData()
person.updatePersonData({"name" : "Spidy", "age": 21})
person.printPersonData()

print(dir(person))
print(persondata)
