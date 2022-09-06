count = 0
for i in range(100, 10000):
    a = i // 1000 #1-я цифра
    b = (i // 100) % 10 #2-я цифра
    c = (i // 10) % 10 #3-я цифра
    d = i % 10 #4-я цифра
    if not (a==b or a==c or a==d or b==c or b==d or c==d):
        count += 1
        # print(i, end=', ') вывод последовательности   
print(f"Количество целых чисел с разными числами = {count}")
        
