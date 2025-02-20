def bigger_is_greater(w):
    w = list(w)
    n = len(w)
    pivot = -1
    
    for i in range(n - 2, -1, -1):
        if w[i] < w[i + 1]:
            pivot = i
            break
    
    if pivot == -1:
        return "no answer"
    
    for i in range(n - 1, pivot, -1):
        if w[i] > w[pivot]:
            break
    
    w[pivot], w[i] = w[i], w[pivot]
    
    w[pivot + 1:] = sorted(w[pivot + 1:])
    
    return ''.join(w)
9
t = int(input("Enter the number : "))
for _ in range(t):
    w = input().strip()
    result = bigger_is_greater(w)
    print(result)
