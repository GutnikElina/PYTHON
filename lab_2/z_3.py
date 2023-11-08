""" Найти сумму каждого столбца матрицы размером m*n """

def get_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            break
        except ValueError:
            print("\n----- Ошибка при вводе данных -----")
            print("-------- Попробуйте снова ---------\n")
    return user_input

m = get_input("Введите количество строк матрицы: ", int)
n = get_input("Введите количество столбцов матрицы: ", int)

matrica = []
for i in range(m):
    row = []
    for j in range(n):
        element = get_input(f"Введите элемент a[{i}][{j}] матрицы: ", int)
        row.append(element)
    matrica.append(row)

for row in matrica:
    for element in row:
        print(element, end=' ')
    print()

for i in range(n):
    column_sum = sum(row[i] for row in matrica)
    print(f"Сумма {i+1}-го столбца: {column_sum}")
