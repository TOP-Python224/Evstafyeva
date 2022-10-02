# Упражнение 105. Произвольные системы счисления
def int2random(number1: int,
               radix1 = '16'):
    """Преобразовывает числа из десятичной системы счисления в 2-, 8-, 16-ную.
    
    
    Параметр основания произвольной системы счисления должен быть строго ключевым
    со значением по умолчанию равным 16."""
    if radix1 == '2':
        number2 = bin(number1)[2:]
        return number2
    if radix1 == '8':
        number2 = oct(number1)[2:]
        return number2
    if radix1 == '16':
        number2 = hex(number1)[2:]
        return number2
    else:
        print('Error')

res1_1 = int2random(15, '2')
res1_2 = int2random(15, '8')
res1_3 = int2random(15)
print(f'{res1_1 = }')
print(f'{res1_2 = }')
print(f'{res1_3 = }')
print()

# res1_1 = '1111'
# res1_2 = '17'
# res1_3 = 'f'

def random2int(number3: str,
               radix2 = '16'):
    """Преобразовывает числа из 2-, 8-, 16-нoй в десятичноую систему счисления.
    
    
    Параметр основания произвольной системы счисления должен быть строго ключевым
    со значением по умолчанию равным 16."""
    if radix2 == '2':
        number4 = int(number3, 2)
        return number4
    if radix2 ==  '8':
        number4 = int(number3, 8)
        return number4
    if radix2 == '16':
        number4 = int(number3, 16)
        return number4
    else:
        print('Error')  

res2_1 = random2int('1010', '2')
res2_2 = random2int('34', '8')
res2_3 = random2int('80')
print(f'{res2_1 = }')
print(f'{res2_2 = }')
print(f'{res2_3 = }')

# res2_1 = 10
# res2_2 = 28
# res2_3 = 128
