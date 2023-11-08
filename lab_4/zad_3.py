"""Реализуйте базовый класс Car. 1. У класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction), которые
должны сообщать, что машина поехала, остановилась, повернула (куда); 2. Опишите
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; 3. Добавьте в
базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
4. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость: {self.speed} км/ч.")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость: {self.speed} км/ч.")

class PoliceCar(Car):
    pass

town_car = TownCar(70, "красная", "Городская машина", False)
town_car.go()
town_car.show_speed()
town_car.turn("влево")
town_car.stop()

print()

sport_car = SportCar(100, "синяя", "Спортивная машина", False)
sport_car.go()
sport_car.show_speed()
sport_car.turn("вправо")
sport_car.stop()

print()

work_car = WorkCar(50, "зеленая", "Рабочая машина", False)
work_car.go()
work_car.show_speed()
work_car.turn("назад")
work_car.stop()

print()

police_car = PoliceCar(90, "белая", "Полицейская машина", True)
police_car.go()
police_car.show_speed()
police_car.turn("вперед")
police_car.stop()
