import random
# Python Basics

"""
Multi line 
commit
"""

# printing statement
print("Hello World")
print("Hello World"[1:3])
print("Hello World"[:3])
print("Hello World"[2:])
print(">>","Hello World"[-5:-1])

# Format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Variables
num1 = 10
num2 = 20
print(num1 ,"+", num2, "=", num1 + num2)

# Type casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)

x = 5
y = "John"
print(type(x))
print(type(y))

# random
print(random.randrange(0,10))
