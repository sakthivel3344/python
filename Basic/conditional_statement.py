# conditional statement

# age = int(input("Enter a number: "))
age = 21
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("hello" in "every one hello all")
print("hello" not in "every one hello all")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not a > b:
  print("a is NOT greater than b")