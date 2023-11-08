"""Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета,
Время вылета, Дни недели. Создать список объектов. Вывести: a) список рейсов
для заданного пункта назначения; b) список рейсов для заданного дня недели"""

class Airline:
    def __init__(self, destination, flight_number, aircraft_type, departure_time, weekdays):
        self.destination = destination
        self.flight_number = flight_number
        self.aircraft_type = aircraft_type
        self.departure_time = departure_time
        self.weekdays = weekdays

    def display_info(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер рейса: {self.flight_number}")
        print(f"Тип самолета: {self.aircraft_type}")
        print(f"Время вылета: {self.departure_time}")
        print(f"Дни недели: {', '.join(self.weekdays)}")

airlines = [
    Airline("Москва", "AB123", "Boeing 737", "12:00", ["Понедельник", "Среда", "Пятница"]),
    Airline("Лондон", "BA456", "Airbus A320", "14:30", ["Вторник", "Четверг"]),
    Airline("Париж", "DC789", "Boeing 777", "16:45", ["Среда", "Пятница"]),
    Airline("Рим", "AZ987", "Airbus A350", "10:15", ["Понедельник", "Среда", "Суббота"]),
]

destination = "Москва"
print(f"\nСписок рейсов для пункта назначения '{destination}':")
for airline in airlines:
    if airline.destination == destination:
        airline.display_info()

weekday = "Среда"
print(f"\nСписок рейсов для дня недели '{weekday}':")
for airline in airlines:
    if weekday in airline.weekdays:
        airline.display_info()
        print()