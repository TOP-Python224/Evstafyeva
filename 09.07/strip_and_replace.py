from random import choice
from string import ascii_letters as asl, digits, punctuation, whitespace

while True:
    str_data = ''.join(
        choice((
            choice(asl), 
            choice(digits), 
            choice(punctuation),
            choice(' \t\n')
        ))
        for _ in range(10)
    )
    print(f'\n{"str_data".rjust(20)} = {str_data!r}')

    str_data_stripped = str_data.strip(punctuation)
    print(f'{"str_data_stripped".rjust(20)} = {str_data_stripped!r}')

    str_data_replaced = str_data
    for c in punctuation:
        str_data_replaced = str_data_replaced.replace(c, '')
    print(f'{"str_data_replaced".rjust(20)} = {str_data_replaced!r}')

    if input('\n _ продолжить? '):
        break
print('\n')


files = [
    'HW.txt',
    'logo.jpg',
    'Python224.csv',
    'Python224_журнал.xlsx',
    'Python224_журнал_тест.xlsx'
]
for file in files:
    file_stem = file.rstrip(asl)[:-1]
    print(f'{file_stem = }')
    file_replaced = file[::-1].replace('_', '-', 1)[::-1]
    print(f'{file_replaced = }\n')
