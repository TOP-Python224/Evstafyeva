# Упражнение 105. Произвольные системы счисления

# ИСПРАВИТЬ: int — это сокращение от integer, что означает целое число; а в python это слово является названием типа — так что ваше название функции вводит в заблуждение
def int2random(number1: int,
               # ИСПРАВИТЬ: это не строго ключевой, а позиционно-ключевой параметр — и почему его значение по умолчанию задаётся строкой? основание системы счисления как раз должно быть числом
               radix1='16'):
    # ИСПРАВИТЬ: согласно заданию преобразование должно быть в произвольную систему счисления в диапазоне от 2 до 16 включительно
    """Преобразовывает числа из десятичной системы счисления в 2-, 8-, 16-ную.

    Параметр основания произвольной системы счисления должен быть строго ключевым со значением по умолчанию равным 16."""
    # ИСПРАВИТЬ: всё это замечательно, но не отвечает условиям задачи
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


def random2int(number3: str,
               # ИСПРАВИТЬ: это не строго ключевой, а позиционно-ключевой параметр — и должен быть числом
               radix2='16'):
    # ИСПРАВИТЬ: согласно заданию преобразование должно быть из произвольной системы счисления в диапазоне от 2 до 16 включительно
    """Преобразовывает числа из 2-, 8-, 16-нoй в десятичную систему счисления.

    Параметр основания произвольной системы счисления должен быть строго ключевым со значением по умолчанию равным 16."""
    if radix2 == '2':
        number4 = int(number3, 2)
        return number4
    if radix2 == '8':
        number4 = int(number3, 8)
        return number4
    if radix2 == '16':
        number4 = int(number3, 16)
        return number4
    else:
        print('Error')

# ДОБАВИТЬ: ещё одну функцию, которая будет использовать две предыдущих и таким образом преобразовывать из любой в любую систему счисления через десятичную

# КОММЕНТАРИЙ: пояснения к математике перевода чисел между системами счисления
#  https://inf.e-alekseev.ru/text/Schisl_perevod.html


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

res2_1 = random2int('1010', '2')
res2_2 = random2int('34', '8')
res2_3 = random2int('80')
print(f'{res2_1 = }')
print(f'{res2_2 = }')
print(f'{res2_3 = }')

# res2_1 = 10
# res2_2 = 28
# res2_3 = 128


# ИТОГ: переписать — 1/5


# СДЕЛАТЬ: остальные задачи!
