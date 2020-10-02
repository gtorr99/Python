def bubble(ls):
    for i in range(len(ls)):
        swapped = False

        for j in range(len(ls) - 1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                swapped = True
        if not swapped: break
    return ls
# if there wasn't any swap it's because the list is aready sorted


a = [15, 20, 12, 16, 10, 14]
print(bubble(a))

