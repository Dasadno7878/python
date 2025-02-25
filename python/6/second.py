n = int(input("Введите натур число n: "))
for i in range(1, n + 1):
    square = i * i
    if str(i) == str(square)[-len(str(i)):]:
        print(i)