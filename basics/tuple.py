# A read-only list
tuple = ('first element', 3, 4.5)

print(tuple)
print(tuple[1:3])

# tuple[0] = 'hello' -> can't update a tuple

del tuple
print(tuple)  # <class 'tuple'>

tuple = (1.5, 3.1, 2.2)

print(len(tuple))
print(max(tuple))
print(min(tuple))

