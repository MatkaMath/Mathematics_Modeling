#Adding noisy data to the given polynomial function and finding the polynomial fit for the set of noisy data. Visualising the function, noisy data and polynomial fit

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.linspace(-2, 2, 100)

# True polynomial function y = -3x^3 + 2x^2 - 1
true_coefficients = [-3, 2, 0, -1]
y_true = np.polyval(true_coefficients, x)

noise = np.random.normal(0, 3, size=y_true.shape)
y_noisy = y_true + noise

coefficients = np.polyfit(x, y_noisy, 3)

polynomial = np.poly1d(coefficients)

y_fitted = polynomial(x)

plt.figure(figsize=(8, 6))
plt.scatter(x, y_noisy, color='red', label='Noisy Data', alpha=0.5)
plt.plot(x, y_true, color='blue', label='True Function', linewidth=2)
plt.plot(x, y_fitted, color='green', label='Fitted Polynomial', linewidth=2)
plt.title('Polynomial Fitting Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
