"""Найти оценки уравнения регрессии, используя метод наименьших
квадратов и матричную форму записи уравнений ..."""

import numpy as np

X = np.column_stack((np.ones(12), np.arange(5, 5 + 12), np.random.randint(60, 83, size=12)))
Y = np.random.uniform(13.5, 18.6, size=(12, 1))
print("Матрица признаков: \n", X)
print("Вектор-столбец значений: \n", Y)

A = np.linalg.inv(X.T @ X) @ (X.T @ Y)

print("Вектор оценок А: ")
print(A)
