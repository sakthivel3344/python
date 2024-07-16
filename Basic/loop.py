# Loops


# For Loop
for x in "banana":
    print(x, end="")
print()

thislist = ["apple", "banana", "cherry"]

for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

newlist = [x for x in range(10)]

print(newlist)


# While Loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")