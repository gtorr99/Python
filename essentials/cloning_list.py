a = [1,4]
c = a.copy() # creates a copy of a
b = a # b points to the same address as a

a[1] = 5

print("a =",a)
print("b =",b)
print("c =",c)
