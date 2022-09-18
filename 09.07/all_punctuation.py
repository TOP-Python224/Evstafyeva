puncs = set()
for i in range(2**15):
    c = chr(i)
    if c.isprintable() and not (c.isalnum() or c.isspace()):
        puncs.add(c)

print(*puncs, end='\n\n')
print(len(puncs))
