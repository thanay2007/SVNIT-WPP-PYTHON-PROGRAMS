import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5

def bisection(f, a, b, tol=1e-6, max_iter=100):
    updates = []
    for _ in range(max_iter):
        c = (a + b) / 2
        updates.append([a, b, c, f(a), f(b), f(c)])
        if f(c) == 0 or (b - a)/2 < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return np.array(updates)

a, b = np.random.uniform(-5, 5, 2)
while f(a) * f(b) > 0:
    a, b = np.random.uniform(-5, 5, 2)

updates = bisection(f, a, b)

plt.figure(figsize=(10, 6))
x_vals = np.linspace(min(a,b)-1, max(a,b)+1, 400)
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
for i, (a_i, b_i, c_i, fa, fb, fc) in enumerate(updates):
    plt.plot([a_i, b_i], [fa, fb], 'rx')
    plt.plot(c_i, fc, 'bo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
