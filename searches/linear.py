def linear_search(a, x):
    n = len(a)
    for i in range(0, n):
        if(a[i] == x):
            return i
    return -1

a = [3, 6, 78,90, 23, 45]
x = int(input("Enter te number to be searched: "))

result = linear_search(a, x)
print(x, "position:", result if result != -1 else "Element doesn't exist")
