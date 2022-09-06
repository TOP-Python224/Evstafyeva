n = input('Введите любое целое число:')
result = ""
for i in range(0, len(n)): 
    if n[i] != '3' and n[i] != '6': 
        result += n[i]
print (result)
