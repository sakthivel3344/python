"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# int
num1 = 1

# float
num2 = 10.5

# string
str1 = 'Hello'
print("string len", len(str1))
print(str1[0])

# List
arr1 = [1,2,3]
print(arr1[0],len(arr1))
arr1.reverse()
print(arr1)
arr2 = range(6)
print(arr2)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # make a copy of the list thislist
mylist = list(thislist) # another way to make a copy of the list thislist
print(mylist)


# Tuple
tuple1 = (1,2,3)
tuple1 = (1,2)
print(tuple1)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])

# update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
del thistuple # to delete the touple

# Dictionary
dict1 = {
    "name":"Sakthivel A",
    "age": 21,
    "age":31
}
print(dict1, dict1["name"])

thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# This will print the keys in the dicrionary
for x in thisdict:
   print(x)

for x in thisdict.values():
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

thisdict.pop("model") # removes the key-value from the dictionary
thisdict.popitem() # removes the last inserted item from the dictionary

thisdict.clear()

# Sets
# Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

thisset.add("orange")

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

mylist = ["kiwi", "orange"]

thisset.update(mylist)

for x in thisset:
  print(x)

# Sets - union
  
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # set3 = set1 | set2

print(set3)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) # myset = set1 | set2 | set3 |set4
print(myset)

# Sets - interseption

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) # set3 = set1 & set2
print(set3) 

# Sets - difference
'''
method will return a new set that will contain only the items 
from the first set that are not present in the other set
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) # set3 = set1 - set2

print(set3)