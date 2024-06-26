# ####################################################

# List: ordered, mutable, allow duplicate elements

# ####################################################

myList = ['banana', "cherry", "apple"]
print(myList)

item = myList.pop()
print(item)
print(myList)

myList.reverse()

print(myList)

myList.sort()

print(myList)

myList = [0] * 5
print(myList)

# -------------------Slicing----------------------

myList = [1, 2, 4, 5, 6, 2, 3, 8]
a = myList[1:4]
print(a)
# step
a = myList[::2]
print(a)
# reverse using step
a = myList[::-1]
print(a)

# --------Deep copy-------
# myList.copy | list(myList) | myList[:]

a = myList.copy()
myList.clear()
print(myList)
print(a)

# Advance - Copy list
myList = [1, 2, 3, 4, 5]
a = [i * i for i in myList]
print(a)
