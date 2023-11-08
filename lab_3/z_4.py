"""Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка будет содержать данные о фирме: название, форма собственности,
выручка, издержки. Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000,
“firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста. """

import json

profit_data = {}
total_profit = 0

with open("firm_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    data = line.strip().split()
    name = data[0]
    revenue = float(data[2])
    expenses = float(data[3])
    profit = revenue - expenses

    if profit > 0:
        profit_data[name] = profit
        total_profit += profit
    else:
        profit_data[name] = "Убыток"

num_profitable_firms = len([profit for profit in profit_data.values() if profit != "Убыток"])
average_profit = total_profit / num_profitable_firms if num_profitable_firms > 0 else 0

result_list = [profit_data, {"Ср. прибыль": average_profit}]

with open("firm_profit.json", "w", encoding="utf-8") as json_file:
    json.dump(result_list, json_file, ensure_ascii=False, indent=4)

print("Результат сохранен в firm_profit.json")