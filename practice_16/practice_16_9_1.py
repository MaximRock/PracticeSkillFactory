"""Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры.
Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры.
Например, для прямоугольника это будут аргументы x, y, width и height.
Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
Создайте метод, который возвращает атрибуты вашей фигуры в виде строки. """

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Стороны треугольника: a = {self.a}, b = {self.b}, c = {self.c}'


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Стороны прямоугольника: a = {self.a}, b = {self.b}'

triangle_1 = Triangle(15, 20, 22)
rectangle_1 = Rectangle(20, 45)

print(str(triangle_1))
print('--------------------------------------------')
print(str(rectangle_1))
