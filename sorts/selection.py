def selection_sort(ls):
    for i in range(len(ls)):
        min = i

        for j in range(i + 1, len(ls)):
            if ls[min] > ls[j]:
                min = j

        ls[i], ls[min] = ls[min], ls[i]
    
    return ls

ls = [5,3,1,8,0,6,9]
print(selection_sort(ls))