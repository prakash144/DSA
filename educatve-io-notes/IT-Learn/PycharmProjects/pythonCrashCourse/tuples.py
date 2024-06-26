# ####################################################

# Tuple: ordered, immutable, allow duplicate elements

# Tuple is more efficient than List in terms of size and latency

# ####################################################

# Declaration
myTuple = ("Max", 28, "tuples", "Max")
myTuple2 = "Max", 28
myTuple3 = ("Max",)
print(type(myTuple3))
myTuple4 = tuple(["Max", 12, "India"])
print(myTuple4)
print(myTuple4[1])
# Invalid
# myTuple4[2] = 200

for i in myTuple:
    print(i)

if "Max" in myTuple:
    print("Yes")
else:
    print("no")

print(len(myTuple))
print(myTuple.count("Max"))
print(myTuple.index("Max"))

myList = list(myTuple)
print(myList)
myTuple = tuple(myList)
print(myTuple)

myTuple5 = "Max", 28, "India"
name, age, city = myTuple5
print(name)
print(age)
print(city)

myTuple5 = (1, 2, 3, 4, 5, 6)

i1, *i2, i3 = myTuple5
print(i1)
print(i3)
print(i2)


