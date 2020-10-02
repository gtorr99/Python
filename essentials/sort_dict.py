# Sorting dictionary items by key or value

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

for i in sorted(x):
    print((i, x[i]))

byValue = sorted(x.items(), key=lambda kv: kv[1])
print(byValue)
