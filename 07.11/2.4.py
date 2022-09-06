# 1 способ

n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))

if n1 > 0 and n2 > 0 and n3 > 0:
    print(n1 + n2 + n3)
elif n1 < 0 and n2 > 0 and n3 > 0:
    print(n2 + n3)
elif n1 < 0 and n2 < 0 and n3 > 0:
    print(n3)
elif n1 > 0 and n2 < 0 and n3 > 0:
    print(n1 + n3)
elif n1 < 0 and n2 > 0 and n3 < 0:
    print(n2)
elif n1 > 0 and n2 > 0 and n3 < 0:
    print(n1 + n2)
elif n1 > 0 and n2 < 0 and n3 < 0:
    print(n1)
else:
    print('Все введенные числа отрицательные')

#2 способ

n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))

if n1 > 0:
    a1 = n1
else: 
    a1 = 0
if n2 > 0:
    a2 = n2
else: 
    a2 = 0
if n3 > 0:
    a3 = n3
else: 
    a3 = 0
    
print(a1 + a2 + a3)
    