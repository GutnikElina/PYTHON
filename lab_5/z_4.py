import numpy as np
import matplotlib.pyplot as plt


def f(x, a):
    return (1/np. tan(x))**3 + 2.24*a*x


a_values = np.arange(-5, 12.5, 0.5)
x_value = 3.567

# Вычисление значений функции для каждого a
f_values = [f(x_value, a) for a in a_values]

# Вывод значений аргумента и значения функции
for a, f_val in zip(a_values, f_values):
    print(f"a = {a:.2f}, f(x) = {f_val:.2f}")

# Нахождение наибольшего, наименьшего и среднего значений
max_val = np.max(f_values)
min_val = np.min(f_values)
avr_val = np.mean(f_values)

# Вывод результатов
print((f"\nМаксимальное значение: {max_val:.2f}"))
print(f"Минимальное значение:{min_val:.2f}")
print(f"Среднее значение: {avr_val:.2f}")
print(f"Количество элементов массива: {len(f_values)}")

# Сортировка массива по возрастанию
sorted_indicies = np.argsort(f_values)
sorted_a_values = a_values[sorted_indicies]
sorted_f_values = np.array(f_values)[sorted_indicies]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sorted_a_values, sorted_f_values, marker='o', label='f(x)')
plt.axhline(y=avr_val, color='r', linestyle='--', label='Среднее значение f(x)')
plt.title('График функции и прямой')
plt.xlabel('Значения a')
plt.ylabel('Значения f(x)')
plt.legend()
plt.grid(True)
plt.show()
