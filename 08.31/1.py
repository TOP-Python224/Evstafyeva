# Напишите функцию высшего порядка, которая принимает объект функции, динамический список аргументов для переданной функции и логический ключ.
# В зависимости от значения логического ключа ФВП возвращает объект float (False) либо str (True, по-умолчанию) – в обоих случаях значение должно быть округлено до двух знаков после запятой
# Вызовите написанную функцию, передав ей lambda-функцию
# Подсказка: в lambda-функции опишите простые математические функции, например, линейную функцию f(x) = kx + b, параболическую g(x) = ax^2 + bx + c, и т.п.
# Протестируйте с различными lambda-функциями и наборами аргументов





# Eсли у коэффициентов a, b, c в анностации указать тип str (в данном варианте кода), 
# функция возвращает None, поэтому заменила тип str на int
from random import randrange as rr
import random

def math_func(a, b, c: int | float) -> bool:
    """Возвращает True или False в зависимости от типа входных параметров функции f(x) = a*x**2 + b*x + c."""
    lambda x: a*x**2 + b*x + c
    if type(x) is int:
        return True
    if type(x) is float:
        return False
        
a, b, c = [rr(1, 10) for _ in range(3)]
print(f'{a, b, c = }')
x = random.choice([rr(1, 20), round(random.uniform(1.1, 19.9), 2)])
print(f'{x = }')
f = math_func(a, b, c)
print(f)

# a, b, c = (2, 9, 8)
# x = 14
# True

# a, b, c = (5, 1, 2)
# x = 10.17
# False