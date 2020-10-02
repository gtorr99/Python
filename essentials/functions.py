def my_func():
    print("This is my function")

my_func()

def argFunc(a, b):
    print("Value of a is", a,"and b is", b)

# required args    
argFunc(1, 2)

# keyword args
argFunc(b=3, a=2)

def sum(a,b,c=0): # c=0 default value
    print(a+b+c)

sum(1,2)

def sum1(*num): # To provide any number of args
    sum=0
    for n in num:
        sum += n
    print('sum is', sum)

# variable length args
sum1(10, 20)

def sub(a,b):
    return a-b

result = sub(2, 1)


def calculate(a, b):
    sum  = a+b
    diff = a-b
    prod = a*b
    quot = a/b

    return sum, diff, prod, quot

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

s,d,p,q = calculate(a,b)

print("\nSum: {} \nDifference: {} \nProduct: {} \nQuotient: {}"
                                                .format(s,d,p,q))
