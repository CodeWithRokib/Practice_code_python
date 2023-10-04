x = 5; # x is the type of int
y = "Rokib" #y is the type of string

print(x)
print(y)

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

x = 5;
y = "rokib"
print(type(x))
print(type(y))

#assign multiple varibales
x,y,z = "orange","Banaa",'Cherry'
print(z)
print(y)
print(x)

##multiple variable using  array
fruits = ["apple",'banana','chery']
x,y,z = fruits
print(x)
print(y)
print(z)

#output operators
x = "Rokib "
y = "hasan "
z = ("Rokib")
print(x+y+z)

#number assign
x = 10
y = 20
print(x+y)

#functional global variabale
x = 'awesome'
def myFunc():
    print('Python is: '+x)

myFunc()