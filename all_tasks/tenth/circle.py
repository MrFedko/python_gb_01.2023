from math import pi
import decimal


class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius
        self.__circle_long: (decimal, None) = None
        self.__area: (decimal, None) = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        self._radius = radius

    @property
    def circle_long(self) -> decimal:
        return decimal.Decimal(pi * self.radius * 2 if self.__circle_long is None else self.__circle_long)

    @property
    def area(self) -> decimal:
        return decimal.Decimal(pi * pow(self.radius, 2) if self.__area is None else self.__area)


if __name__ == '__main__':
    new_circle = Circle(12)
    print(new_circle.circle_long)
    print(new_circle.area)
