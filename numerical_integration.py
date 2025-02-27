# For the given function calculates the numerical integration using Simpson's rule and visualize the result
# Compares the result from Simpson's rule to result from SciPy's quad function
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2 * np.pi * x)

def simpsons_rule(func, a, b, n):
    if n % 2 == 1:  # n must be even
        n += 1
    x = np.linspace(a, b, n+1)
    y = func(x)
    h = (b - a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])

a = 0
b = 1
n = 10 

simp_result = simpsons_rule(f, a, b, n)

# Value of the integral using SciPy's quad function
quad_result, _ = spi.quad(f, a, b)

# Absolute error
simp_error = abs(simp_result - quad_result)

print(f"Simpson's Rule Result: {simp_result}, Error: {simp_error}")
print(f"SciPy's quad Result: {quad_result}")

x_values = np.linspace(a, b, 1000)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = sin(2πx)', color='blue')

x_simp = np.linspace(a, b, n+1)
y_simp = f(x_simp)
plt.fill_between(x_simp, y_simp, alpha=0.3, label='Simpson\'s Area', color='green')

plt.title('Numerical Integration of f(x) = sin(2πx)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()