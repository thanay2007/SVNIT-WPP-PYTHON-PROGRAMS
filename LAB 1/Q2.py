import random
l = []
longest_zero_row = []
zero_row = 0

for i in range(0, 100):
    l.append(random.randint(0, 1))

for i in range(0, 100):
    if l[i] == 0:
        zero_row += 1
    else:
        longest_zero_row.append(zero_row)
        zero_row = 0

print(l)
print("Largest number of zeroes in a row:", max(longest_zero_row))
