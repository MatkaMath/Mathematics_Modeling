# Comparing linear and cubic interpolation methods for the given set of data points
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 1, 4, 1, 0, 1])

linear_interp = interp1d(x_data, y_data, kind='linear')

cubic_interp = interp1d(x_data, y_data, kind='cubic')

x_fine = np.linspace(0, 5, 100)

y_linear = linear_interp(x_fine)
y_cubic = cubic_interp(x_fine)

plt.figure(figsize=(10, 5))
plt.scatter(x_data, y_data, color='red', label='Data Points', zorder=5)
plt.plot(x_fine, y_linear, label='Linear Interpolation', linestyle='--')
plt.plot(x_fine, y_cubic, label='Cubic Interpolation', linestyle='-')
plt.title('Interpolation of Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()
