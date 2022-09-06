number = int(input('Введите трехзначное число > ')) #127
n1 = number % 10 #7
n2 = (number // 10) % 10 #2
n3 = number // 100 #1

print(f"Сумма цифр равна {n1 + n2 + n3}")
print(f"Произведение цифр равно {n1 * n2 * n3}")

