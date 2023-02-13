from random import randint


def binary_random_search(minimum: int, maximum: int, count: int) -> bool:
    num = randint(minimum, maximum + 1)
    search_num = None
    while search_num != num:
        search_num = int(input("Угадайте число: "))
        print([["Загаданное число меньше", "Загаданное число больше"][search_num < num], "Угадали!"][search_num == num])
        count -= 1
        if count == 0:
            print("Попытки закончились")
            return False
    return True
