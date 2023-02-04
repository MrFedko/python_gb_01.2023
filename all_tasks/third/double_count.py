def double_count(my_list: list) -> list:
    return list(filter(lambda x: my_list.count(x) != 2, my_list))
