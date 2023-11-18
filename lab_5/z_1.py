# Вычисления с помощью NumPy

import numpy as np

a = 0.94
x = 0.093

z = np.arccos(x**2) - a * np.sqrt(x) + (np.sin(np.pi/2 + a)**3) / np.log(2 * x)
print("\nВыражение равно: ", z)
