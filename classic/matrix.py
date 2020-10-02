def transpose(matrix):
    t = [ 
          [0, 0, 0],
          [0, 0, 0]
        ]

    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            t[row][col] = matrix[col][row]
    return t

matrix = [
          [2,3],
          [3,4],
          [9,0]
         ]

print(transpose(matrix))

def matrix_addtion(a, b):
    c = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    for col in range(len(a)):
        for row in range(len(a[col])):
            c[row][col] = a[row][col] + b[row][col]
    return c

a = [
        [3, 4, 7],
        [4, 7, 5],
        [9, 8, 2]
    ]

b = [
        [7, 3, 2],
        [7, 0, 4],
        [1, 8, 3]
    ]

print(matrix_addtion(a, b))
