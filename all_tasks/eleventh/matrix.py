from functools import total_ordering


@total_ordering
class Matrix:
    def __init__(self, matrix: list[list]):
        self.value = matrix
        self.length = len(matrix)
        self.height = len(matrix[0])

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, matrix: list[list]):
        self._value = matrix

    def __str__(self):
        return "\n".join(str(i) for i in self.value)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.value[i][j] == other.value[i][j])
                return all(result)
        return False

    def __lt__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.value[i][j] < other.value[i][j])
                return all(result)
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = [[] for i in range(self.length)]
                for i in range(self.length):
                    for j in range(self.height):
                        result[i].append(self.value[i][j] + other.value[i][j])
                return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.length:
                result = [[sum(a * b for a, b in zip(self_row, other_col))
                           for other_col in zip(*other.value)]
                          for self_row in self.value]
            elif self.length == other.height:
                result = [[sum(a * b for a, b in zip(self_col, other_row))
                           for self_col in zip(*self.value)]
                          for other_row in other.value]
            return Matrix(result)
        return False


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix_1, matrix_2, sep='\n\n')
    print(matrix_1 == matrix_2)
    print(matrix_1 == matrix_3)
    print(matrix_1 < matrix_2)
    print(matrix_1 > matrix_2)
    add_matrix = matrix_1 + matrix_2
    print(add_matrix)
    mul_matrix = matrix_1 * matrix_2
    print(mul_matrix)
