from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return (self.side1 + self.side2 + self.side3) / 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


triangle = Triangle(10, 20, 30)
rectangle = Rectangle(10, 20)
