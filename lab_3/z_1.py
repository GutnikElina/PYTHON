""" Создать программный файл F1 в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
Скопировать из файла F1 в файл F2 строки, начиная с четвертой
по порядку. Подсчитать количество символов в последнем слове F2. """

with open("F1.txt", "w") as file1:
    while True:
        line = input("Введите строку (для окончания ввода оставьте строку пустой): ")
        if line == '':
            break
        file1.write(line + "\n")

with open("F1.txt", "r") as file:
    print("Файл F1")
    for string in file:
        print(string)

with open("F1.txt", "r") as file1, open("F2.txt", "w") as file2:
    lines = file1.readlines()
    for line in lines[3:]:
        file2.write(line)

with open("F2.txt", "r") as file:
    print("Файл F2")
    for string in file:
        print(string)

with open("F2.txt", "r") as file2:
    words = file2.read().split()
    last_word = words[-1]
    count = len(last_word)

print(f"Количество символов в последнем слове F2: {count}")
