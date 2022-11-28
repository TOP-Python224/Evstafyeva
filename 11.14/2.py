class Point:
    """Описывает точку на плоскости в декартовой системе координат."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    """Описывает отрезок, задаваемый двумя точками на плоскости в декартовой системе координат."""
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point

    @property
    def length(self) -> float:
        return ((self.end_point.x - self.start_point.x)**2 + (self.end_point.y - self.start_point.y)**2)**0.5


class Polygon:
    """Описывает многоугольник, задаваемый отрезками на плоскости в декартовой системе координат."""
    def __init__(self,
                 side1: Line,
                 side2: Line,
                 side3: Line,
                 *sides: Line):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = sides

    def _is_closed(self) -> bool:
        if (self.side1.start_point.x == self.side3.end_point.x
                and self.side1.start_point.y == self.side3.end_point.y
                or self.side1.start_point.x == self.sides.end_point.x
                and self.side1.start_point.y == self.sides.end_point.y):
            return True
        else:
            return False

    @property
    def perimetr(self) -> float:
        # if Polygon._is_closed is True:
        # Как и в задаче 1 столкнулась с проблемой применения методов, которые работают с типами bool.
        # Помогите разобраться.
            return self.side1.length + self.side2.length + self.side3.length
        # Если добавляю + self.sides.length, то выдает ошибку "AttributeError: 'tuple' object has no attribute 'length'"
        # Как написать код, чтобы он работал вместе с *args?
        # else:
        #     print('Многоугольник разомкнут')


# тест
p1 = Point(5.1, 7.9)
p2 = Point(8, 12)
p3 = Point(7.05, 0.9)

l1 = Line(p1, p2)
l2 = Line(p2, p3)
l3 = Line(p3, p1)
print(l1.length)
print(l2.length)
print(l3.length)

pol1 = Polygon(l1, l2, l3)
print(pol1.perimetr)
