from uniq_list import uniq
from string_from_user import reformat
from type_dict import get_type_dict
from double_count import double_count

if __name__ == "__main__":
    # get uniq numbers
    print(uniq([int(i) for i in input("Введите целые числа через пробел: ").split()]))

    # check type of text
    result = reformat(input("Введите данные: "))
    print(result, type(result))

    # dict of types
    my_tuple = (1, 2, "any", "text", 1.34, 5.23, [1, 2, 3, 4, 5], [2, 3, 4], (1, 2), (3, 4))
    print(get_type_dict(my_tuple))

    # delete double count elements
    my_list = [1, 2, 3, 4, 1, 5, 3, 3]
    print(double_count(my_list))
