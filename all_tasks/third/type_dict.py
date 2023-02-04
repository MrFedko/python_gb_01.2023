def get_type_dict(corteg: tuple) -> dict:
    result = {}
    for i in corteg:
        result.setdefault(type(i), [])
        result[type(i)].append(i)
    return result
