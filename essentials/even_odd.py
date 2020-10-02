list_num = [1,2,3,4,5,6,7,8]

even = lambda a: a % 2 == 0
odd = lambda a: a % 2 != 0

even_list = list(filter(even, list_num))
odd_list  = list(filter(odd, list_num))

print(even_list)
print(odd_list)

