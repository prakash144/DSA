# ####################################################

# Strings : ordered, immutable, text representation

# ####################################################

myString = "Hello World"
print(myString)

# Reverse
subString = myString[::-1]
print(subString)

myString = "How,are,you,doing"
myList = myString.split(",")
print(myList)
newString = ' '.join(myList)
print(newString)

# Example with Time

from timeit import default_timer as timer
myList = ['a'] * 5
print(myList)

# bad
start = timer()
myString = ''
for i in myList:
    # create new string and then assign back, costly operation
    myString +=i
stop = timer()
print(myString)
print(stop-start)

# good
start = timer()
myString = ''.join(myList)
stop = timer()
print(myString)
print(stop-start)

# Format String
#  %, .format, f-strings
print("--------------Format String-------------")
varStr = "Tom"
varInt = 3
varFloat = 3.146767

# Old style
myString = "the variables are %.2f" % varFloat
print(myString)

myString = "the variable are {}, {}, and {:.2f}".format(varStr, varInt, varFloat)
print(myString)

# New Style
myString = f"the variable are {varStr}, {varInt*3}, and {varFloat}"
print(myString)



