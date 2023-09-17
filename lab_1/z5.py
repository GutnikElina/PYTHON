"""Реализуйте программу «Магазин игрушек», которая будет
включать в себя шесть пунктов меню. У вас есть словарь, где ключ –
название игрушки. Значение – список, который содержит состав
игрушки, цену и кол-во (шт),которое есть в магазине. """

toys = {"Мяч": ["Резина", 10.99, 5],
    "Кукла": ["Фарфор", 15.99, 8],
    "Лего": ["Пластик", 20.99, 7],
    "Пазл": ["Картон", 12.99, 10],
    "Вертолет": ["Металл", 29.99, 2],
    "Машинка": ["Пластмасса", 8.99, 6]}

def menu():
    print('''\n  ===  МАГАЗИН ИГРУШЕК   ==  \n1) Просмотр состава игрушки\n2) Просмотр цены
3) Просмотр количества\n4) Всю информацию\n5) Покупка\n6) Выход''')

def print_quality():
    print("\n --- Состав игрушек ---")
    for toy, details in toys.items():
        print(f"{toy}: {details[0]}")

def print_price():
    print("\n --- Цена игрушек ---")
    for toy, details in toys.items():
        print(f"{toy}: {details[1]}")

def print_quantity():
    print("\n --- Количество игрушек ---")
    for toy, details in toys.items():
        print(f"{toy}: {details[2]}")

def print_all():
    print("\n --- Вся информация о игрушках ---")
    for toy, details in toys.items():
        print(f"Название: {toy}")
        print(f"Качество: {details[0]}")
        print(f"Цена: {details[1]}")
        print(f"Количество: {details[2]}")
        print("--------------------------")

def purchase():
    total_price = 0
    while True:
        toy = input("Введите название игрушки (или 'n' для выхода): ")
        if toy == "n":            break
        quantity = int(input("Введите количество: "))
        if toy in toys:
            price = toys[toy][1]
            remaining_quantity = toys[toy][2]
            if quantity <= remaining_quantity:
                total_price += price * quantity
                toys[toy][2] -= quantity
                print("\nВы добавили товар в корзину! ")
                print(f"\tВыбранный товар: {toy}\n\t"
                      f"Количество товара: {quantity}\n\t"
                      f"Стоимость: {price * quantity}")
                print("Продолжим? \n")
            else:
                print(f"В магазине нет такого количества товара '{toy}'")
        else:
            print("Такой игрушки нет в магазине:(")
    print("\n============== ЧЕК ==============")
    print(f"Общая стоимость покупки: {total_price}")
while True:
    menu()
    choice = input("\nВаш выбор: ")
    if choice == "1":
        print_quality()
    elif choice == "2":
        print_price()
    elif choice == "3":
        print_quantity()
    elif choice == "4":
        print_all()
    elif choice == "5":
        purchase()
    elif choice == "6":
        print("\n  ==  ХОРОШЕГО ДНЯ  ==  \n")
        break
    else:
        print("\nНеверный номер пункта меню! Попробуйте снова\n")
