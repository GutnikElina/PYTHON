import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Первый график
z = x**0.25 + y**0.25
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.title('z = x^{0.25} + y^{0.25}')
plt.show()

# Второй график
z = x**2 - y**2
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.title('z = x^2 - y^2')
plt.show()

# Третий график
z = 2*x + 3*y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.title('z = 2x + 3y')
plt.show()

# Четвертый график
z = x**2 + y**2
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.title('z = x^2 + y^2')
plt.show()

# Пятый график
z = 2 + 2*x + 2*y - x**2 - y**2
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
plt.title('z = 2 + 2x + 2y - x^2 - y^2')
plt.show()
