def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while(first <= last and not found):
        mid = (first + last) // 2
        if list[mid] == item:
            found = True
        elif list[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return found

ls = [1,3,4,5,8]
x = 4

print(binary_search(ls, x))
