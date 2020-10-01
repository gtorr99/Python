a = ' Hello Python '

print(a)
print(type(a)) # str

print(a[0:4])  # prints from x to y char
print(a[5:])   # prints from x to the end

print(a*2)  # prints the string twice
print(len(a)) 

print(a.strip()) # equals to trim
print(a.lstrip())
print(a.rstrip())

print(a.find("py")) # returns -1 if doesn't find
print(a.find("Py")) 
print(a.count("l")) # counts till first "l"

print(a.replace("Python", "world"))
print(a)

print(a.split())
print(a.split(" "))

print(a.upper())
print(a.lower())
print(a.title())

str = "Python"
print(reversed(str))  # <reversed object at 0x000002556D524C70>
s = ''
print(s.join(reversed(str))) # reverses a string
