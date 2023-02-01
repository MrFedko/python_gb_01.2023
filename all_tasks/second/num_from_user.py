def get_number(number: int, mod: int = 10) -> str:
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


if __name__ == "__main__":
    print(get_number(*[int(i) for i in
                input("Введите число и систему исчисления в которой хотите его представить (через пробел): ").split()]))

