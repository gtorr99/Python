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


def matrix_multiplication(a, b):
    c = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    for rowA in range(len(a)):
        for colB in range(len(b[0])):
            for rowB in range(len(b)):
                c[rowA][colB] += a[rowA][rowB] * b[rowB][colB]
    return c

a = [
        [2, 7, 3],
        [5, 9, 2],
        [5, 13, 10]
    ]

b = [
        [5, 8, 1, 9],
        [6, 7, 8, 0],
        [4, 5, 10, 1]
    ]

print(matrix_multiplication(a, b))
print(len(a))
print(len(a[0]))
print(len(b))
print(len(b[0]))