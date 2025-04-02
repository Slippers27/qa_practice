total = 0

while True:
    x = 0
    try:
        x = float(input("Введите число: "))
    except ValueError:
        print("Ошибка, можно вводить только цифры")
        continue
    if x != 0:
        total += x
    else:
        print("Окончание вычислений")
        break

print("Сумма чисел:", total)