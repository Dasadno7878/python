import math

def main():
    # Ввод размера матрицы
    n = int(input("Введите размер матрицы n: "))
    
    # Создаём пустую матрицу R
    R = []
    
    
   
    for i in range(n):
        row = []
        for j in range(n):
            value = math.cos((i+1)**2 + (j+1))**3
            row.append(value)
        R.append(row)
    
    # Находим минимальный элемент третьего столбца
    
    if n >= 3:
        third_column = [R[i][2] for i in range(n)]
        min_third_column = min(third_column)
    else:
        min_third_column = None  # Если матрица меньше 3x3
    
    # Сумма элементов первой строки 
   
    if n >= 1:
        sum_first_row = sum(R[0])
    else:
        sum_first_row = None
    
    # Заменяем отрицательные элементы матрицы R на их модули
    for i in range(n):
        for j in range(n):
            if R[i][j] < 0:
                R[i][j] = abs(R[i][j])
    
    # Вывод результатов
    print("\nМатрица R (после замены отрицательных значений на модули):")
    for row in R:
        print(row)
    
    if min_third_column is not None:
        print(f"\nМинимальный элемент третьего столбца: {min_third_column}")
    else:
        print("\nТретьего столбца в матрице нет.")
    
    if sum_first_row is not None:
        print(f"Сумма элементов первой строки: {sum_first_row}")
    else:
        print("Первой строки в матрице нет.")


main()
