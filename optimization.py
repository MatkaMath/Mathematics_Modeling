import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Step 1: Define the function to minimize
def objective_function(x):
    return (x - 1)**2 + 3

# Step 2: Use SciPy's minimize function to find the minimum
initial_guess = 0  # Starting point for the optimization
result = minimize(objective_function, initial_guess)

# Step 3: Extract the optimal value and the minimum function value
optimal_x = result.x[0]
minimum_value = result.fun

# Step 4: Print the results
print("Optimal x:", optimal_x)
print("Minimum value of the function:", minimum_value)

# Step 5: Plot the function and the minimum point
x_values = np.linspace(-4, 6, 100)
y_values = objective_function(x_values)

plt.plot(x_values, y_values, label='f(x) = (x - 1)^2 + 3')
plt.scatter(optimal_x, minimum_value, color='red', label='Minimum Point', zorder=3)
plt.title('Optimization of the Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=minimum_value, color='gray', linestyle='--', label='Minimum Value')
plt.axvline(x=optimal_x, color='gray', linestyle='--')
plt.legend()
plt.grid()
plt.show()
