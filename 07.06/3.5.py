number = int(input('Введите четырехзначное число > ')) #1273
n1 = number % 10 #3
n2 = (number // 10) % 10 #7
n3 = (number // 100) % 10 #2
n4 = number // 1000 #1

print(f"Зеркальное ему число: {n1}{n2}{n3}{n4}")

