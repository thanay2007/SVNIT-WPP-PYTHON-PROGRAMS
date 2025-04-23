import numpy as np

arr = np.array(['Thanay', 'Yash', 'Teja', 'Sambhav'])
length = 15

centered = np.char.center(arr, length, fillchar='_')
left = np.char.ljust(arr, length, fillchar='_')
right = np.char.rjust(arr, length, fillchar='_')

print("Original array:")
print(arr)
print("\nCentered:")
print(centered)
print("\nLeft-justified:")
print(left)
print("\nRight-justified:")
print(right)
