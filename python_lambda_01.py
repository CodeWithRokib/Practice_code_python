x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


#using function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))