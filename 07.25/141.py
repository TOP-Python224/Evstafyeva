n = int(input('Введите число от 0 до 999: '))

units = {1: 'one', 2: 'two', 3: 'three', 
         4: 'four', 5: 'five', 6: 'six', 
         7: 'seven', 8: 'eight', 9: 'nine'}
         
teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 
         14: 'fourteen', 15: 'fifthteen', 16: 'sixteen', 
         17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
         
tens = {10: 'ten', 20: 'twenty', 30: 'thirty',
        40: 'fourty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninty'}  
        
hundreds = {100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 
            400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 
            700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'}
            

n1 = n % 10 #единицы
n2 = n - n1 #десятки без единиц
n3 = ((n // 10) % 10) * 10 #десятки
n4 = n - n3 - n1 #сотни
n5 = n % 100 
n6 = n % 1000 

if (n < 10): 
    print(units.get(n)) #вывод чисел от 1 до 9

#двузначные числа     
elif 10 < n < 20: 
    print(teens.get(n)) #вывод чисел от 11 до 19    
elif (n1 == 0): 
    print(tens.get(n)) #вывод целых десятков 20, 30 ...90    
elif (20 < n < 100): 
    print(tens.get(n2) + ' ' + units.get(n1)) #вывод остальных двузначных чисел
    
#трехзначные числа   
elif (n5 in teens):
    print(hundreds.get(n4) + ' ' + teens.get(n5)) #вывод таких чисел как 215, 514, 711   
elif (n1 in units):
    print(hundreds.get(n4) + ' ' + units.get(n1)) #вывод таких чисел как 305, 204, 709     
elif (n3 in tens):
    print(hundreds.get(n4) + ' ' + tens.get(n3) + ' ' + units.get(n1)) #вывод остальных двузначных чисел работает некорректно, не видит десятки. Почему???
else: 
    print(hundreds.get(n)) #вывод целых cотен 200, 300 ...900 работает некорректно, выдает None. Почему??? 
