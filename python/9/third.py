def pozitnum(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            else:
                print("Число должно быть положительным.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

def floatlist(size, prompt):
    arr = []
    for i in range(size):
        while True:
            try:
                num = float(input(f"{i + 1}: "))
                arr.append(num)
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")
    return arr

n1 = pozitnum("Введите количество элементов в первом массиве: ")
array1 = floatlist(n1, "Введите элемент первого массива")

n2 = pozitnum("Введите количество элементов во втором массиве: ")
array2 = floatlist(n2, "Введите элемент второго массива")

k = -1
while not (0 <= k < len(array1)):
    try:
        k = int(input("Введите позицию k для вставки второго массива: "))
        if not (0 <= k < len(array1)):
            print(f"Значение k должно быть от 0 до {len(array1) - 1}.")
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")

for i in range(len(array2)):
    array1.insert(k + i, array2[i])

print(array1)