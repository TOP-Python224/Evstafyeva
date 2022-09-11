string = set(input('Введите строку: '))
# print(string) 

binary_number = {'0', '1', 'b'}
if string <= binary_number:
    print(f'ДА')
else: 
    print(f'НЕТ') 


# Введите строку: 12
# НЕТ

# Введите строку: b0110
# ДА