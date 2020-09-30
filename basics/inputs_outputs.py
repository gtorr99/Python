a = 10
b = 15
c = 20
t = 'The value of a is'


print(t, a)
print(a,b,c)
print(a,b,c, sep=',')
print(a,b,c, end=',')

name = "Gabriel" 
age = 21

print('\nMy name is', name, "and I'm", age, "years old.")
print("\nMy name is %s and I'm %d years old." %(name, age))
print("\nMy name is {} and I'm {} years old." .format(name, age))

# i = int(input("Enter something: "))
# print("You have entered:", i)

list = [x for x in input("Enter the elements: ").split(sep=",")]
print("List:", list)


