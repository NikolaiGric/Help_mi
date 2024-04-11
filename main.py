import math


class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        semiperimeter = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            semiperimeter * (semiperimeter - self.side1) * (semiperimeter - self.side2) * (semiperimeter - self.side3))

    def is_right_triangle(self):
        return self.side1 ** 2 + self.side2 ** 2 == self.side3 ** 2 or \
            self.side1 ** 2 + self.side3 ** 2 == self.side2 ** 2 or \
            self.side2 ** 2 + self.side3 ** 2 == self.side1 ** 2
