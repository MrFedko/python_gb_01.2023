from all_tasks.triangle import Triangle
from all_tasks.prime_or_composite import is_prime

if __name__ == "__main__":
    a, b, c = (float(input(f"Введите {i + 1} сторону треугольника ")) for i in range(3))
    any_triangle = Triangle(a, b, c)

    try:
        print(any_triangle, any_triangle.type, sep='\n')
    except AttributeError:
        print("Попробуйте ещё раз")


    number: int = -1
    while number < 0 or number > 100_000:
        number = int(input("Введите число от 0 до 100_000 "))
    print(["Это составное число", "Это простое число"][is_prime(number)])
