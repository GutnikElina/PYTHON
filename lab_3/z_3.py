"""
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб)
                     Физика:   30(л)    10(лаб)
                     Физкультура:      30(пр)
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open('schedule.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

subjects = {}

for line in lines:
    hours = 0
    subject_lesson = line.split(':')
    lesson = subject_lesson[1].strip().split()

    for les in lesson:
        if "(л)" in les:
            hours += int(les.split("")[0])
        elif "(пр)" in les:
            hours += int(les.split("(пр)")[0])
        elif "(лаб)" in les:
            hours += int(les.split("(лаб)")[0])

    subjects[subject_lesson[0]] = hours

print(subjects)

