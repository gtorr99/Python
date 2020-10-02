# Armstrong number: the sum of each digit raised to the nth order 
# is equals to the number
# Ex.: 152 = 1^3 + 5^3 + 2^3 (order = 3)

def order(x):
    n = 0
    while x != 0:
        n += 1
        x //= 10
    return n

def is_armstrong(x):
    n = order(x)
    temp = x
    sum = 0

    while temp != 0:
        r = temp % 10
        sum += pow(r,n)
        temp //= 10
    
    print(sum)
    return sum == x

print(is_armstrong(153))
print(is_armstrong(1332))
