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


if __name__ == '__main__':
    new_rectangle = Rectangle(12)
    print(new_rectangle.perimetr)
    print(new_rectangle.area)
