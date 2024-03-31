#accessing an item in a tuple
myTuple = ("green","orange","white","red")
print(myTuple[1])
print(myTuple[:1])

#adding an item in a tuple
myTupleAdd =myTuple + ("black","pink")
print(myTupleAdd)

#removing items from a tuple
x = list(myTuple)
print(x)
y = x.remove("green")
print(x)
y = tuple(myTuple)
print(myTuple)

