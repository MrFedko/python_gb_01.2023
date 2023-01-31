from all_tasks.triangle import Triangle
from all_tasks.prime_or_composite import is_prime
from all_tasks.binary_search import search
from all_tasks.circle import Circle
from all_tasks.negative_discr import negative

if __name__ == "__main__":
    # Triangle
    a, b, c = (float(input(f"Введите {i + 1} сторону треугольника ")) for i in range(3))
    any_triangle = Triangle(a, b, c)

    try:
        print(any_triangle, any_triangle.type, sep='\n')
    except AttributeError:
        print("Попробуйте ещё раз")

    #is_prime
    number: int = -1
    while number < 0 or number > 100_000:
        number = int(input("Введите число от 0 до 100_000 "))
    print(["Это составное число", "Это простое число"][is_prime(number)])

    #search
    search()

    #Circle
    number: (float) = float(input("Введите диаметр круга: "))
    krug = Circle(number)
    print(f"Длинна окружности = {krug.circle_long:.42f} \nПлощадь круга = {krug.area:.42f}")

    #negative discrim
    result = negative(*[complex(i) for i in input("Введите a, b, c через пробел: ").split()])
    print(f"D = {result[0]} \nx1 = {result[1]} \nx2 = {result[2]}")
