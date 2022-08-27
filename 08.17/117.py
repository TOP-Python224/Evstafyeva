# Упражнение 117. ТОлько слова

text = input('Введите строку: ')

prepared = ''
for char in text:
    if char not in '.,:;!?—…"':
        prepared += char
           
print(prepared.split(" "))

# "Contractions include: don’t, isn’t, and wouldn’t."
# ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']
