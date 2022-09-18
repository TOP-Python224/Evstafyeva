from random import choice
from string import ascii_letters as asl

words = [
    ''.join(choice(asl) for _ in range(10))
    for _ in range(1000000)
]

for word in words:
    # применять, когда выброс исключения случается редко
    try:
        # применять, когда мы полностью или почти полностью уверены в существовании подстроки в исходной строке
        i = word.lower().index('word')
    except ValueError:
        i = None
    # применять, когда мы не уверены в существовании подстроки в исходной строке
    j = word.lower().find('word')
    print(f'{word}   {i = }   {j = }')
    
    if i:
        break

else:
    print('\n _ не найдено! =( ')


text = 'information school graduate seeks graduate school information'

i = text.find('school')

j = text.find('school', 30)
j = text[30:].find('school')

k = text.find('school', 20, 40)
k = text[20:40].find('school')

print(i, j, k)
