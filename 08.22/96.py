# Упражнение 96. Является ли строка целым числом?

def isInteger(text: str) -> bool:
    """Определяет, является ли введенная строка целочисленным значением."""
    text_1 = text.split(' ')
    print(text_1)
    text_2 = ''.join(text_1)
    print(text_2)
    # print(text_2[0])
    while text_2[0] == '+' or text_2[0] == '-':
        if len(text_2)>= 1 and text_2[1:len(text_2)].isdecimal():
            return True
        else:
            return False
 
text_pre = input('Введите строку: ')
res = isInteger(text_pre)
print(res)