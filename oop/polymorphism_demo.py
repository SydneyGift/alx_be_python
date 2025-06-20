from math import pi
class Shape:
    def __init__(self):
        pass
    def area (self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area (self):
        area = self.length * self.width
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = pi * (self.radius **2)
        return area