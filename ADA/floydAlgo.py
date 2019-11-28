import numpy as np
def floyd(matrix,n):
    new = matrix
    print(new)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])

    print(np.array(matrix))

matrix = [[0,2,9999,1,8],
          [6,0,3,2,9999],
          [9999,9999,0,4,9999],
          [9999,9999,2,0,3],
          [3,9999,9999,9999,0]]

floyd(matrix,5)