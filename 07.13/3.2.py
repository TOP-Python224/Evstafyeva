count = 0
for i in range(100, 1000):
    x = i// 100
    y = (i % 100)*10
    z = i % 10
    if x == y or x == z or y == z:
        # print(i, end=', ') вывод последовательности
        count += 1   
print(f"Количество целых чисел с одинаковыми цифрами = {count}")     