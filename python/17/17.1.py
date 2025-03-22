def main():
    # Ввод массива Q (8 элементов)
    Q = []
    print("Введите 8 элементов массива Q (целые числа):")
    for i in range(8):
        val = int(input(f"Q[{i}]: "))
        Q.append(val)

    # Ввод массива R (7 элементов)
    R = []
    print("\nВведите 7 элементов массива R (целые числа):")
    for i in range(7):
        val = int(input(f"R[{i}]: "))
        R.append(val)

    # Вывод исходных массивов
    print("\nИсходные массивы:")
    print("Q:", Q)
    print("R:", R)

    # 1. 
    Q.append(33)
    print("\nПосле добавления 33 в Q:", Q)

    # 2. 
    if len(Q) > 1:
        Q.pop(1)
    print("После удаления второго элемента из Q:", Q)

    # 3. 
    if len(R) >= 2:
        R.insert(2, 88)
    print("После вставки 88 в R:", R)

    # 4. 
    QR1 = Q + R
    print("\nНовый массив QR1 (объединение Q и R):", QR1)

    # 5. 
    QR1.sort(reverse=True)
    print("QR1 после сортировки по убыванию:", QR1)

    # 6. 
   
    try:
        position_33 = QR1.index(33) + 1  # позиция с учётом 1-based
        print(f"Позиция числа 33 в QR1 (считая с 1): {position_33}")
    except ValueError:
        print("Число 33 не найдено в массиве QR1.")

    # 7. 
    
    QR2 = []
    for i in range(len(QR1)):
        if (i + 1) % 3 == 0:
            QR2.append(QR1[i])
    print("\nМассив QR2 (элементы, стоящие на позициях, кратных 3):", QR2)

    # 8. 
    if len(QR2) > 1:
        QR2 = [QR2[-1]] + QR2[:-1]
    print("QR2 после сдвига элементов на 1 вправо:", QR2)

main()
