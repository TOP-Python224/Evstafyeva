number = int(input('Введите трехзначное число > ')) #542
n1 = number % 10 #2
n2 = (number // 10) % 10 #4
n3 = number // 100 #5

print(f"Сумма цифр равна {n1 + n2 + n3}")
print(f"Произведение цифр равно {n1 * n2 * n3}")

