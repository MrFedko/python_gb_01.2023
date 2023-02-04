def uniq(numbers: list) -> list:
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
