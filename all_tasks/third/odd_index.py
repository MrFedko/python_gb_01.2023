def odd_index(my_lst: list[int]) -> list:
    return [i for i, j in filter(lambda x: x[1] & 1 != 0, enumerate(my_lst, 1))]
