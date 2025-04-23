import numpy as np

inputs = []
for i in range(5):
    user_input = input(f"Enter string {i+1} (or press Enter to stop): ")
    if not user_input:
        break
    inputs.append(user_input)

if not inputs:
    inputs = ['default1', 'default2', 'default3']

arr = np.array(inputs)

centered = np.char.center(arr, 15, fillchar='_')
left = np.char.ljust(arr, 15, fillchar='_')
right = np.char.rjust(arr, 15, fillchar='_')

print("\nCentered:")
print(centered)
print("\nLeft-justified:")
print(left)
print("\nRight-justified:")
print(right)
