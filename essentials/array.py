def split_array(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]
        arr[n-1] = x

arr = [12, 10, 7, 34]
n = len(arr)
position = 2

split_array(arr, n, position)
print(arr)