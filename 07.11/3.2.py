year = int(input('Является ли год високосным? Введите год:'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Да')
else:
    print('Нет')  