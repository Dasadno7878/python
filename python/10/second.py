matrix = [
    [6, 1, 8],
    [7, 5, 3],
    [2, 9, 4]
]

N = len(matrix)

center = matrix[N // 2][N // 2]
maxdiag = matrix[0][0]
maxdiagpos = (0, 0)
for i in range(N):
    if matrix[i][i] > maxdiag:
        maxdiag = matrix[i][i]
        maxdiagpos = (i, i)

max2diag = matrix[0][N - 1]
max2diagpos = (0, N - 1)
for i in range(N):
    if matrix[i][N - 1 - i] > max2diag:
        max2diag = matrix[i][N - 1 - i]
        max2diagpos = (i, N - 1 - i)

if maxdiag > max2diag:
    max_element = maxdiag
    max_pos = maxdiagpos
else:
    max_element = max2diag
    max_pos = max2diagpos

matrix[max_pos[0]][max_pos[1]], matrix[N // 2][N // 2] = matrix[N // 2][N // 2], matrix[max_pos[0]][max_pos[1]]

for row in matrix:
    print(row)