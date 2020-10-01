list = ['hello', 145, 1.2]

print(list)
print(list[0])
print(list[1:3])
print(list[1:])


list2 = ['xyz', 122]
list_new = list + list2

print(list_new)

list[2] = 45
print(list)

del list[2]
print(list)

list.append("Python")
print(list)

print(list.index("Python"))

list_sum = [2,3,4,5]
print(sum(list_sum))      # 14
print(sum(list_sum, 10))  # 24
