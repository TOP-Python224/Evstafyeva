#1 способ
text = list(input('Введите текст телеграммы: '))
x = ' '
l = len(text) - text.count(x)
print (f"{(80*l) // 100} руб. {(80*l) % 100} коп.")



#2 способ
text = input('Введите текст телеграммы: ')
text1 = text.split()
a = ''
text2 = a.join(text1)
l = len(text2)
print (f"{(80*l) // 100} руб. {(80*l) % 100} коп.")
