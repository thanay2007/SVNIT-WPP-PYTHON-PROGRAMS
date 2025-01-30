l = []

for i in range(1, 27):
    str = ''
    for j in range(i):
        str += chr(96 + i)
    l.append(str)

print(l)
