from circle import Circle
from negative_discr import negative
from hex_number import hex_number
from fractions_from_user import UserFractions

if __name__ == "__main__":
    # Circle
    number: (float) = float(input("Введите диаметр круга: "))
    krug = Circle(number)
    print(f"Длинна окружности = {krug.circle_long:.42f} \nПлощадь круга = {krug.area:.42f}")

    # negative discrim
    result = negative(*[complex(i) for i in input("Введите a, b, c через пробел: ").split()])
    print(f"D = {result[0]} \nx1 = {result[1]} \nx2 = {result[2]}")

    # int to hex
    number: int = int(input("Введите число: "))
    print(f'''hex of number = {hex_number(number)}
test with hex() = {hex(number)}''')

    # fractions from user
    fraction_1, fraction_2 = [UserFractions(*[int(j) for j in i.split("/")])
                              for i in input("Введите две дроби формата a/b через пробел: ").split()]

    print(f"""Вы ввели дроби {fraction_1} и {fraction_2}
{fraction_1} + {fraction_2} = {fraction_1 + fraction_2}
{fraction_1} * {fraction_2} = {fraction_1 * fraction_2}""")
