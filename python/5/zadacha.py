while True:
    protect = input("Введите число k: ")
    if protect.isdigit():
        k = int(protect)
        break
    else:
        print("Ошибка: введите только цифры.")

posld = ""
num = 2

while len(posld) < k:
    posld += str(num)
    num += 2

print(f"{k}-я цифра последовательности: {posld[k - 1]}")