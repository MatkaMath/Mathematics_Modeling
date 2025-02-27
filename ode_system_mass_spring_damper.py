# Modeling a mass spring damper system and solving the system of ordinary differential equations
# Plotting displacement and velocity over time
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 1.0  # mass (kg)
k = 10.0  # spring constant (N/m)
b = 0.5  # damping coefficient (kg/s)

def model(y, t):
    x, v = y
    dydt = [v, -b/m * v - k/m * x]
    return dydt

x0 = 1.0
v0 = 0.0 
y0 = [x0, v0]

t = np.linspace(0, 10, 100)

solution = odeint(model, y0, t)

x = solution[:, 0]
v = solution[:, 1]

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, x, 'b', label='Displacement (x)')
plt.title('Mass-Spring-Damper System')
plt.ylabel('Displacement (m)')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v, 'r', label='Velocity (v)')
plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
