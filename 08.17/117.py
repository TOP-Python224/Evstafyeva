# Упражнение 117. ТОлько слова

text = input('Введите строку: ')

prepared = ''
# ИСПРАВИТЬ: такой подход как раз удалит все знаки препинания, включая те, которые находятся посередине слов — вместо этого необходимо использовать метод strip(), который удаляет нужные символы только в начале и конце строки
for char in text:
    if char not in '.,:;!?—…"':
        prepared += char
           
print(prepared.split(" "))


# stdout:
# "Contractions include: don’t, isn’t, and wouldn’t."
# ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']


# ИТОГ: нужный строковый метод не использован — 1/3
