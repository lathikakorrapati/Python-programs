import numpy as np
try:
    matrix = [[1, 2, 3],
          [4, 1, 6],
          [7, 8, 6]]
    m = np.array(matrix)
    inverse_matrix = np.linalg.inv(m)
    print("inverse_matrix:\n",inverse_matrix)
except np.linalg.LinAlgError:
    print("error")