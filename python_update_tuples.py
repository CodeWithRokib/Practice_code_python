x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#;conver the tuplpe into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


#create new tuple with the value

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)