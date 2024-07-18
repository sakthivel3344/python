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
  "year": 1964,
  "model": "Mustang",
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