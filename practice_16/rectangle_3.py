from practice_16_8_2 import Rectangel, Square, Circle
from math import pi

# Создаем прямоугольник
rect_1 = Rectangel(3,4)

# Создаем квадрат
square_1 = Square(5)

# Создаем круг
circle_1 = Circle(2, pi)

# Создаем колекцию для наших фигур
figures = [rect_1, square_1, circle_1]

for figure in figures:
    if isinstance(figure, Square):
        print('Площадь квадрата =', figure.get_area_square())
    elif isinstance(figure, Rectangel):
        print('Площадь прямоугольника =', figure.get_area())
    else:
        print('Площадь круга =', ('{:.3f}'.format(figure.get_area_circle())))




