# HCF: Highest Common Factor
def hcf(x, y):
    while(y):
        x , y = y, x%y
    return x

list = [a for a in input("Enter 2 numbers: ").split()]
print(hcf(int(max(list)), int(min(list))))
