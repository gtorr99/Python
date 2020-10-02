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
