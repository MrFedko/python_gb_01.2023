from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, height: float, width: float = 0):
        self.height: float = height
        self.width: float = [width, height][width == 0]
        self.__perimetr: (float, None) = None
        self.__area: (float, None) = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: float):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: float):
        self._width = width

    @property
    def perimetr(self) -> float:
        if self.__perimetr is None:
            self.__perimetr = (self.height + self.width) * 2
        return self.__perimetr

    @property
    def area(self) -> float:
        if self.__area is None:
            self.__area = self.height * self.width
        return self.__area

    def __add__(self, other):
        new_perimetr = self.perimetr + other.perimetr
        new_height = self.height + other.height
        new_width = new_perimetr/2 - new_height
        return Rectangle(new_height, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr - other.perimetr)
        new_height = abs(self.height - other.height)
        new_width = new_perimetr/2 - new_height
        return Rectangle(new_height, new_width)

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area


if __name__ == '__main__':
    rectangle1 = Rectangle(2)
    rectangle2 = Rectangle(4, 5)
    new_rec = rectangle1 + rectangle2
    print(new_rec.width, new_rec.height, new_rec.perimetr)
    new_new_rec = rectangle1 - rectangle2
    print(new_new_rec.width, new_new_rec.height, new_new_rec.perimetr)
