Упражнение 118. Словесные палиндромы

1. Неправильно поняла задание и изначально сделала решение для буквенного палиндрома

text = input('Введите строку: ')

prepared = ''
for char in text.lower():
    if char not in ' .,:;!?—…"':
        prepared += char          
# print(prepared)

reversed_text = ''.join(reversed(prepared))
# print(reversed_text)

if reversed_text == prepared:
    print ("Палиндром")
else:
    print ("Не палиндром")
# А муза рада музе без ума да разума
# Палиндром



