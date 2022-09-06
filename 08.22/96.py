# Упражнение 96. Является ли строка целым числом?

# ИСПРАВИТЬ: имя функции в snake_lower_case (текстовый курсор на имя функции и Shift+F6)
def isInteger(text: str) -> bool:
    """Определяет, является ли введенная строка целочисленным значением."""
    # ОТВЕТИТЬ: вы решили проигнорировать все пробелы в строке, а не только ведущие и замыкающие?
    # ИСПРАВИТЬ: используйте строковый метод strip()
    text_1 = text.split(' ')
    print(text_1)
    # КОММЕНТАРИЙ: обратите внимание, что переменную text_1 вы больше не используете, следовательно можно её перезаписать новым значением, чтобы не увеличивать количество переменных
    text_2 = ''.join(text_1)
    print(text_2)
    # ИСПРАВИТЬ: здесь важна последовательность проверок — вы сначала осуществляете обращение к символу с индексом 0, и только потом проверяете длину строки — а надо наоборот, потому что если пользователь введёт пустую строку, то эта строка выбросит исключение
    # ОТВЕТИТЬ: а почему while, а не if?
    # ИСПРАВИТЬ: в условии задачи сказано, что ведущий знак может присутствовать, а может отсутствовать — а сейчас если функции передать строку, содержащую только цифры, то она вернёт None, потому что даже не зайдёт в цикл
    # ИСПОЛЬЗОВАТЬ: а ещё можно вот так сформулировать условие проверки первого символа строки:
    #               text_2[0] in '+-'
    while text_2[0] == '+' or text_2[0] == '-':
        if len(text_2) >= 1 and text_2[1:len(text_2)].isdecimal():
            return True
        else:
            return False


# СДЕЛАТЬ: не забывайте тестировать ваш код с разными входными данными
text_pre = input('Введите строку: ')
res = isInteger(text_pre)
print(res)


# ДОБАВИТЬ: закомментированный результат вывода в стандартный поток вывода (stdout)
# stdout:
# ...


# СДЕЛАТЬ: и загрузить остальные задачи


# ИТОГ: требуется переработать — 4/7