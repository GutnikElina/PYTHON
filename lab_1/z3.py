"""Найдите наименьший четный элемент списка. Если такого нет, товыведите первый элемент.
Преобразовать список так, чтобы сначала
шли нулевые элементы, а затем все остальные"""

entered_list = input("ВВЕДИТЕ ЭЛЕМЕНТЫ СПИСКА ЧЕРЕЗ ПРОБЕЛ: ").split()
print(entered_list)
entered_list = list(map(int, entered_list))
minimum = min(entered_list, key=lambda x: x if x % 2 == 0 and x != 0 else float('inf'), default=entered_list[0])
entered_list.sort(key=lambda x: x if x == 0 else float('inf'))
print("НАИМЕНЬШИЙ ЧЕТНЫЙ ЭЛЕМЕНТ СПИСКА: ", minimum)
print("ПРЕОБРАЗОВАННЫЙ СПИСОК: ", entered_list)
