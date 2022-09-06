n = list (input('Введите адрес электронной почты: '))
if ('@' in n) and ('.' in n) and (n.index('@') < n.index('.')):
    print('Верно')
else:
    print('Неверно')