# ####################################################

# Dictionary : Key-Value pairs, Unordered, Mutable

# ####################################################

myDict = {"name": "Max", "age": 28, "city": "India"}
print(myDict)

myDict2 = dict(name="Mary", age=27, city="India")
print(myDict2)

myDict["email"] = "max@xyz.com"
print(myDict)

# myDict.pop("email")
del myDict["email"]
print(myDict)

for key, value in myDict.items():
    print(key, value)

# ----------Copy Dict

myDict_copy = dict(myDict)
# myDict_copy = myDict.copy()
print(myDict_copy)


# merge Dict
myDict.update(myDict2)
print(myDict)

# Tuple can be used as Key but not list

myTuple = (1, 2)
myDict3 = {myTuple: "Prakash"}
print(myDict3)



