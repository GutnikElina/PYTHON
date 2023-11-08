"""
Создать текстовый файл (не программно). Построчно записать названия
детских товаров и их стоимость (не менее 10 строк). Вывести на экран
все товары, стоимость которых ниже 10 рублей. Вывести на экран
все товары с минимальной стоимостью.
Пример файла:
Машинка  50
Кукла  40
"""
import codecs

with codecs.open('products.txt', encoding='utf-8') as file:
    lines = file.readlines()

products = {}
print("Все товары, стоимость которых ниже 10 рублей:")

for line in lines:
    name, price = line.strip().split()
    price = float(price)
    products[name] = price
    if price < 10:
        print(line)

min_price = min(products.values())

for name, price in products.items():
    if price == min_price:
        print("Товар с минимальной стоимостью:", name, price)
