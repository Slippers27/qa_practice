a = int (input())
b = int (input())
c = a + b
d = a * b

print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")


if c == d:
    print(f"Результаты вычеслений равны. Получившеесея число = {a * b}")
elif d < c:
    print(f"Наибольшее значение получилось при сложении цифр. Оно равно {c}")
elif d > c:
    print(f"Наибольшее значение получилось при умножении цифр. Оно равно {d}")



