# Упражнение 120. Форматирование списка

text = input('Введите элементы списка через пробел: ')

text_1 = text.split()

text_begin = text_1[0:len(text_1) - 1]
# print(text_begin)
text_end = text_1[len(text_1)-1:]
# print(text_end )

text_2 = ', '.join(text_begin)
# print(text_2)
text_3 = ', '.join(text_end)
# print(text_3)

text_result = text_2 + ' и ' + text_3 
print(text_result)

# яблоко груша апельсин банан
# яблоко, груша, апельсин и банан

