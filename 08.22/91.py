# Упражнение 91. Григорианский календарь в порядковый

def ordinalDate(day: int, 
                month: int, 
                year: int) -> int:
    """Возвращает порядковый номер заданного дня в указанном году."""
    leap_year_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 
                   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    non_leap_year_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: # Проверка года на високосность
        new_list = list(leap_year_months.values())[0:month-1]
        # print(new_list)
        day_number = sum(new_list) + day  
        return day_number 
        # print(day_number)     
    else:
        new_list = list(non_leap_year_months.values())[0:month-1]
        # print(new_list)
        day_number = sum(new_list) + day  
        return day_number 

            
day_1 = int(input('\n > введите день: '))
month_1 = int(input(' > введите месяц: '))
year_1 = int(input(' > введите год: '))
res = ordinalDate(day_1, month_1, year_1)
print(f'\t{res}')