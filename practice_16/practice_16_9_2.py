class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter_rectangle(self):
        return (self.a + self.b) * 2

class Square:
    def __init__(self, a):
        self.a = a

    def perimeter_square(self):
        return self.a * 4

rectangle = Rectangle(15, 25)
square = Square(26)

print(f'Периметр прямоугольника = {rectangle.perimeter_rectangle()} \n'
      f'Периметр квадрата = {square.perimeter_square()}')
