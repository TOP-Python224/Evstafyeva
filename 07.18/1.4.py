number = list(input('Введите номер из шести цифр: ')) #['1', '2', '3', '4', '5', '6']
newlist = []
for element in number:
    newlist.append(int(element))
# print(newlist) #[1, 2, 3, 4, 5, 6]
n1 = newlist[:3]
n2 = newlist[3:]
if sum(n1) == sum(n2):
    print('ДА')
else:
    print('НЕТ')