n = int(input(' > '))
summ = 0
for i in range(n):
    m = int(input())
    if m <= 0:
       m = 0
    else:
       summ += m
print(summ)
