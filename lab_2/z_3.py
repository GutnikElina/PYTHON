""" Найти сумму каждого столбца матрицы размером m*n """


while True:
    try:
        m = int(input("Введите количество строк матрицы: "))
        if m < 1:
            print("\n----- Ошибка при вводе данных -----")
            print("-------- Попробуйте снова ---------\n")
            continue
        break
    except ValueError:
        print("\n----- Ошибка при вводе данных -----")
        print("-------- Попробуйте снова ---------\n")

while True:
    try:
        n = int(input("Введите количество столбцов матрицы: "))
        if n < 1:
            print("\n----- Ошибка при вводе данных -----")
            print("-------- Попробуйте снова ---------\n")
            continue
        break
    except ValueError:
        print("\n----- Ошибка при вводе данных -----")
        print("-------- Попробуйте снова ---------\n")

matrica = []
for i in range(m):
    matrica.append([0]*n)

for i in range(m):
    for j in range(n):
        while True:
            try:
                element = int(input(f"Введите элемент a[{i}][{j}] матрицы: "))
                matrica[i][j] = element
                break
            except ValueError:
                print("\n----- Ошибка при вводе данных -----")
                print("-------- Попробуйте снова ---------\n")

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        print(matrica[i][j], end=' ')
    print()

for i in range(len(matrica[0])):
    summa = 0
    for j in range(len(matrica)):
        summa += matrica[j][i]
    print(f"Сумма {1+i}-го столбца: {summa}")
