from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def search():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    search_num = -1
    count = 10
    while search_num != num:
        search_num = int(input("Угадайте число: "))
        print([["Загаданное число меньше", "Загаданное число больше"][search_num < num], "Угадали!"][search_num == num])
        count -= 1
        if count == 0:
            print("Попытки закончились")
            break

