"""Придумать класс самостоятельно, реализовать в нем методы
экземпляра класса, статические, методы, методы класса."""

import math
class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius**2

    def calculate_circumference(self):
        return 2 * self.pi * self.radius

    @staticmethod
    def convert_to_diameter(radius):
        return 2 * radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

circle = Circle(5)

area = circle.calculate_area()
circumference = circle.calculate_circumference()
print("\nПлощадь окружности:", area)
print("Длина окружности:", circumference)

diameter = Circle.convert_to_diameter(5)
print("Диаметр окружности:", diameter)

circle2 = Circle.from_diameter(8)
area2 = circle2.calculate_area()
print("\nПлощадь второй окружности:", area2)
