def only_double(my_list: list) -> list:
    return list(set(filter(lambda x: my_list.count(x) > 1, my_list)))
