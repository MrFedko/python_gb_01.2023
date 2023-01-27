from all_tasks.triangle import Triangle

if __name__ == "__main__":
    a, b, c = (float(input(f"Введите {i + 1} сторону треугольника ")) for i in range(3))
    any_triangle = Triangle(a, b, c)

    try:
        print(any_triangle, any_triangle.type, sep='\n')
    except AttributeError:
        print("Попробуйте ещё раз")

