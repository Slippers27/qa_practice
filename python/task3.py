sum = 0

while True:
    x = float(input("Введите число: "))
    if x != 0:
        sum += x
    else:
        x == 0
        print("Окончание вычислений")
        break

print("Сумма чисел:", sum)