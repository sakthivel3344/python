import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["name"])


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x) # converst into json

print(y)