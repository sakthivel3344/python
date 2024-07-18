# Iteration with tuple
mytuple = (1,2,3)
myiter = iter(mytuple)

while True:
    try:
        print(next(myiter))
    except:
        print("No item to iterate")
        break

# Iteration with string
mystr = "banana"
myiter = iter(mystr)

print(next(myiter))
print(next(myiter))

# Iteration with class
class MyNumber:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        val = self.num
        self.num += 1
        return val

obj = MyNumber()
myiter = iter(obj)

print(next(myiter))
print(next(myiter))