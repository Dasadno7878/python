numbers = []
while True:
    try:
        N = int(input("Введите количество чисел N: "))
        break
    except ValueError:
        print("Введите целое число. Попробуйте снова.")

while True:
    try:
        K = float(input("Введите число K: "))
        break
    except ValueError:
        print("Введите число. Попробуйте снова.")

for i in range(N):
    while True:
        try:
            num = float(input(f"Введите число {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Введите число. Попробуйте снова.")

minK = sum(1 for num in numbers if num < K)
srK = sum(1 for num in numbers if num == K)
maxK = sum(1 for num in numbers if num > K)

# Вывод результата
print(f"Чисел меньше K: {minK}")
print(f"Чисел равно K: {srK}")
print(f"Чисел больше K: {maxK}")