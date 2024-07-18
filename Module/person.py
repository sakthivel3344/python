persondata = {
    "name": None,
    "age": None,
}

def printPersonData():
    for x in persondata:
        print(f"{x}: {persondata[x]}")

def updatePersonData(data):
    persondata.update(data)
    print("person data updated")
