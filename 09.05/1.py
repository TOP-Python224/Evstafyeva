from random import randrange as rr

list_1 = [rr(11, 25, 2) for _ in range(26)]
list_2 = [rr(1, 25, 5) for _ in range(26)]

s1 = set(list_1)
s2 = set(list_2)

print(f'{s1 = }')
print(f'{s2 = }\n')
print(s1.difference(s2))
print(s2.difference(s1))

# s1 = {11, 13, 15, 17, 19, 21, 23}
# s2 = {1, 6, 11, 16, 21}

# {13, 15, 17, 19, 23}
# {16, 1, 6}


