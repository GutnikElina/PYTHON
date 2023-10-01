# Напишите программу, демонстрирующую работу try\except\finally

while True:
    menu = ["\n======= КАЛЬКУЛЯТОР =======", "1) Сложение", "2) Вычитание", "3) Умножение", "4) Деление", "0) Выход"]

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
    finally:
        print("\n--------Ввод осуществлен--------")

    while 1:
        try:
            a = int(input("\nВведите первое число: "))
            break
        except ValueError:
            print("\n------Такой ввод невозможен-------")

    while 1:
        try:
            b = int(input("\nВведите второе число: "))
            break
        except ValueError:
            print("\n------Такой ввод невозможен-------")

    if choice == 1:
        print("\nСумма чисел: ", a + b)
    elif choice == 2:
        print("\nРазница между числами: ", a - b)
    elif choice == 3:
        print("\nУмножение чисел: ", a * b)
    elif choice == 4:
        try:
            print("\nДеление чисел: ", a / b)
        except ZeroDivisionError:
            print("\n!!! Невозможно деление на 0 !!!")
