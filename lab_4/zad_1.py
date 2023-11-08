"""Создать class Human. Определить у него атрибуты имя и год рождения.
Прописать 2 метода. Первый метод: выводит на экран имя и возраст ,
второй метод : проверяет является ли человек совершеннолетним."""

class Human:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
    def display_info(self):
        current_year = 2023
        age = current_year - self.year_of_birth
        print(f"Имя: {self.name}, Возраст: {age}")

    def is_adult(self):
        current_year = 2023
        age = current_year - self.year_of_birth

        if age >= 18:
            print((f"{self.name} является совершеннолетним"))
        else:
            print(f"{self.name} не является совершеннолетним")

person1 = Human("Анастасия", 1990)
person1.display_info()
person1.is_adult()

person2 = Human("Иван", 2006)
person2.display_info()
person2.is_adult()