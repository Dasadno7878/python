matrix = [
    [1, -2, 3],
    [-4, -5, -6],
    [7, -8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

xarktst = []
for col in range(cols):
    sum_neg_odd = 0
    for row in range(rows):
        element = matrix[row][col]
        if element < 0 and element % 2 != 0:
            sum_neg_odd += abs(element)
    xarktst.append(sum_neg_odd)

sorted_cols = sorted(range(cols), key=lambda x: xarktst[x])

sorted_matrix = [[matrix[row][col] for col in sorted_cols] for row in range(rows)]


print("Исходная матрица:")
for row in matrix:
    print(row)

print("Характеристики столбцов:", xarktst)


print("Отсортированная матрица:")
for row in sorted_matrix:
    print(row)