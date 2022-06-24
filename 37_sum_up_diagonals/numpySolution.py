# Reference to the numpy solution:
# https://stackoverflow.com/questions/35252993/sum-of-diagonal-elements-in-a-matrix

import numpy as np

m1 = [
        [1,   2],
        [30, 40],
    ]
diagonal1 = np.asarray(m1)
antiDiagonal1 = np.fliplr(m1)
print(np.trace(diagonal1 + antiDiagonal1)) # 73

m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
diagonal2 = np.asarray(m2)
antiDiagonal2 = np.fliplr(m2)
print(np.trace(diagonal2 + antiDiagonal2)) # 30
