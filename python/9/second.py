posled = []

while True:
    try:
        n = int(input("Введите количество элементов в последовательности: "))
        if n > 0:
            break
        else:
            print("Количество элементов должно быть положительным числом.")
    except ValueError:
        print("Вы ввели не число. Пожалуйста, попробуйте снова.")

print("Введите элементы последовательности:")
for i in range(n):
    while True:
        try:
            num = float(input(f"{i + 1}-й элемент: "))
            posled.append(num)
            break
        except ValueError:
            print("Вы ввели не число. Пожалуйста, попробуйте снова.")

min_value = min(posled)
max_value = max(posled)

print(f"Минимальное значение в последовательности: {min_value}")
print(f"Максимальное значение в последовательности: {max_value}")

posledKvdrt = []
for ak in posled:
    if ak >= 0:
        posledKvdrt.append(ak * (min_value ** 2))
    else:
        posledKvdrt.append(ak * (max_value ** 2))

print("Преобразованная последовательность:")
for value in posledKvdrt:
    print(value)