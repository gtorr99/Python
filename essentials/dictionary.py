# Dictionary: key-value variable
# Only one key name. If there is more than one, it consideres the last
# You can only update values, not keys

dict = {'name': 'John', 'age' : 25}

print(dict['name'])
print(dict['age'])
print(dict)           # {'name': 'John', 'age': 25}
print(dict.values())  # dict_values(['John', 25])

dict['name'] = 'Rohn'
print(dict['name'])

dict['address'] = 'earth'
print(dict)

print(len(dict))
dict1 = dict.copy()
print(dict1)

dict1['name'] = 'Mohit'

print(dict.items())
# dict_items([('name', 'Rohn'), ('age', 25), ('address', 'earth')])

dict.update(dict1) # updates dict as dict1 values
print(dict)

dict2 = {'height': 160, 'weight': 60}
dict.update(dict2)
print(dict)
#{'name': 'Mohit', 'age': 25, 'address': 'earth', 'height': 160, 'weight': 60}

dict.clear()
print(dict)  # {}

del dict
print(dict)

