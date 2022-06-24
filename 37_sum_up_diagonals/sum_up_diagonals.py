def sum_up_diagonals(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-i-1]
    return total
    

m1 = [
        [1,   2],
        [30, 40],
    ]
print(sum_up_diagonals(m1)) # 73

m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
print(sum_up_diagonals(m2)) # 30