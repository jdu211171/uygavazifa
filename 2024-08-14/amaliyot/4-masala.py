from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self, num):
        pass


class Line(Shape):

    def draw(self, num: int):
        print('* ' * num)


class Triangle(Shape):

    def draw(self, num: int):
        for i in range(1, num + 1):
            for j in range(1, i + 1):
                if j == 1 or j == i or i == num:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


class Square(Shape):

    def draw(self, num):
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                if i == 1 or j == 1 or i == num or j == num:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


class NullShape(Shape):

    def draw(self, num=0):
        print('bo\'sh shakl')


line = Line()
line.draw(10)

triangle = Triangle()
triangle.draw(10)

square = Square()
square.draw(10)

null_shape = NullShape()
null_shape.draw()
