import numpy as np

def create_magic_square(n):
    if n % 2 == 1:
        magic_square = np.zeros((n, n), dtype=int)
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i, j] = num
            new_i, new_j = (i - 1) % n, (j + 1) % n
            if magic_square[new_i, new_j]:
                i = (i + 1) % n
            else:
                i, j = new_i, new_j
    elif n % 4 == 0:
        arr = np.arange(1, n * n + 1).reshape(n, n)
        mask = (arr % 4 == 0) | ((arr // n) % 4 == (arr % n) % 4)
        magic_square = np.where(mask, arr, n * n + 1 - arr)
    else:
        k = n // 2
        A = create_magic_square(k)
        magic_square = np.block([[A, A + 2 * k * k],
                               [A + 3 * k * k, A + k * k]])
        swap_cols = list(range(k // 2)) + [n - 1 - i for i in range((k // 2) - 1)]
        magic_square[:, swap_cols] = magic_square[:, swap_cols][::-1]
    return magic_square

for N in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square (N={N}):")
    print(create_magic_square(N))
