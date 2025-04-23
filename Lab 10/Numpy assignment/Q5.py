import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5

def find_initial_interval(max_attempts=100):
    for _ in range(max_attempts):
        a = np.random.uniform(-10, 10)
        b = np.random.uniform(-10, 10)
        if f(a) * f(b) < 0:
            return min(a,b), max(a,b)
    raise ValueError("Could not find suitable interval")

a, b = find_initial_interval()
tolerance = 1e-6
max_iterations = 100
updates = np.zeros((max_iterations, 3))

for i in range(max_iterations):
    c = (a + b) / 2
    updates[i] = [a, b, c]
    if abs(f(c)) < tolerance:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

updates = updates[:i+1]

x = np.linspace(min(updates[:,0])-1, max(updates[:,1])+1, 400)
plt.plot(x, f(x), label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(updates[:,2], np.zeros_like(updates[:,2]), color='red', label='Midpoints')
plt.plot([updates[0,0], updates[0,1]], [0, 0], 'go-', label='Initial interval')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method Root Finding')
plt.legend()
plt.grid()
plt.show()
