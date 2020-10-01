f = lambda a,b,c: a*b*c
output = f(2,4,5)

print(output)

oldlist = [0,2,3,4,5,6,7,8]
newlist = list(filter(lambda a: (a%2 != 0), oldlist))
print(newlist)

list_true = list(filter(None,oldlist)) # filters only "true" itens
print(list_true)

