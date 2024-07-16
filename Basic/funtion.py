def myFun1(num):
    print("From funtion", num)
    return num

print(myFun1(20))

def my_function_1(*kids):
  print("The youngest child is " + kids[2])

my_function_1("Emil", "Tobias", "Linus")

def my_function_2(child3, child2, child1):
  print("The youngest child is " + child3)

my_function_2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function_3(**kid):
  print("His last name is " + kid["lname"])

my_function_3(fname = "Tobias", lname = "Refsnes")


# lambda function

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))
