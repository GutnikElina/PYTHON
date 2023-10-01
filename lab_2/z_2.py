"""Напишите функцию, которая будет принимать один аргумент.
Если в функцию передаётся множество, то найти сумму всех элементов.
Если список, то найти произведение между первым и вторым
отрицательными элементами. Максимальный и минимальный элемент поменять местами.
Число – сумму цифр.
Строка – вывести на экран самое длинное слово.
Сделать проверку со всеми этими случаями"""

import random

while True:
    menu = ("\n----- Выберите с чем хотите продолжить работу -----", "1) Множество",
            "2) Список", "3) Число", "4) Строка", "0) Выход")

    for i in menu:
        print(i)

    try:
        choice = int(input("\nВаш выбор: "))
        if choice < 0 or choice > 4:
            print("\n------Такой выбор невозможен-------")
            continue
        elif choice == 0:
            break
    except ValueError:
        print("\n------Такой выбор невозможен-------")
        continue

    if choice == 1:
        my_set = set()
        for i in range(5):
            rand_number = random.randrange(-10, 20)
            my_set.add(rand_number)
        print(f"Множество: {my_set}")
        sum_of_elements = sum(my_set)
        print(f"\nСумма всех элементов множества: {sum_of_elements}")
    elif choice == 2:
        l = [int(random.uniform(-100, 100)) for i in range(10)]
        print(f"\nСписок: {l}")
        pr = 1
        k = 0
        for i in l:
            if i < 0 and k < 2:
                pr *= i
                k += 1
        print(f"Произведение первого и второго отрицательного элемента: {pr}")
        maximum = max(l)
        minimum = min(l)
        for i in range(len(l)):
            if l[i] == maximum:
                l[i] = minimum
            elif l[i] == minimum:
                l[i] = maximum
        print(f"После того, как поменяли макс. элемент с мин.: {l}")
    elif choice == 3:
        number = str(random.randrange(100, 1000))
        print(f"\nМаксимальная цифра в числе {number}: ", max(number))
    elif choice == 4:
        sentence = input("\nВведите строку: \n")
        words = sentence.split()
        longest = max(words, key=len)
        print(f"Самое длинное слово: {longest}")
