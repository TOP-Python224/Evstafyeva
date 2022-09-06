n = int(input('Введите целое число: '))    
result = 0
for i in range(n, 0, -1):
    if (n % i == 0):
        result += i
print(f"Сумма всех делителей числа {n} равна: {result}")


    
