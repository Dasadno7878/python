N = int(input("Введите натур. N: "))

sum_digits = 0
temp = N
while temp > 0:
    sum_digits += temp % 10
    temp = temp // 10

M = N + 1
found = False
while M < 2 * N:
    if M % sum_digits == 0:
        found = True
        break
    M += 1

if found:
    print("Наименьшее M:", M)
else:
    print("нет")