import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper = s.str.upper()
lower = s.str.lower()
length = s.str.len()

print("Original Series:")
print(s)
print("\nUppercase:")
print(upper)
print("\nLowercase:")
print(lower)
print("\nLength:")
print(length)
