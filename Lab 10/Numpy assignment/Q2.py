def make_magic_square(n):
    if n % 2 == 1:
        magic_square = [[0] * n for _ in range(n)]
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i][j] = num
            new_i, new_j = (i - 1) % n, (j + 1) % n
            if magic_square[new_i][new_j]:
                i = (i + 1) % n
            else:
                i, j = new_i, new_j
    else:
        magic_square = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if (i < n//2 and j < n//2) or (i >= n//2 and j >= n//2):
                    magic_square[i][j] = n*n + 1 - magic_square[i][j]
    return magic_square

for n in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square for n = {n}:")
    square = make_magic_square(n)
    for row in square:
        print(' '.join(f"{num:3d}" for num in row))
