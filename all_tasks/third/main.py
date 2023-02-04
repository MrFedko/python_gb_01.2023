from uniq_list import uniq
from string_from_user import reformat

if __name__ == "__main__":
    # get uniq numbers
    # print(uniq([int(i) for i in input("Введите целые числа через пробел: ").split()]))

    # check type of text
    result = reformat(input("Введите данные: "))
    print(result, type(result))
