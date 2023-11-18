import numpy as np
import matplotlib.pyplot as plt

# Первый график
# Создаем сетку значений для x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Вычисляем значения функции
z = x**0.25 + y**0.25

# Строим график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Показываем график
plt.title('z = x^{0.25} + y^{0.25}')
plt.show()

# Второй график
# Вычисляем значения функции
z = x**2 - y**2

# Строим график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Показываем график
plt.title('z = x^2 - y^2')
plt.show()

# Третий график
# Вычисляем значения функции
z = 2*x + 3*y

# Строим график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Показываем график
plt.title('z = 2x + 3y')
plt.show()

# Четвертый график
# Вычисляем значения функции
z = x**2 + y**2

# Строим график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Показываем график
plt.title('z = x^2 + y^2')
plt.show()

# Пятый график
# Вычисляем значения функции
z = 2 + 2*x + 2*y - x**2 - y**2

# Строим график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Показываем график
plt.title('z = 2 + 2x + 2y - x^2 - y^2')
plt.show()