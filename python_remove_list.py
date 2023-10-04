thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#remove the last item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

