from math import pi
import decimal


class Circle:
    def __init__(self, diameter: float):
        self.diameter: float = diameter
        self.__circle_long: (decimal, None) = None
        self.__area: (decimal, None) = None

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter: float):
        self._diameter = diameter

    @property
    def circle_long(self) -> decimal:
        return decimal.Decimal(pi * self.diameter if self.__circle_long is None else self.__circle_long)

    @property
    def area(self) -> decimal:
        return decimal.Decimal(pi * pow(self.diameter / 2, 2) if self.__area is None else self.__area)
