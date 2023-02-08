def list_sum(numbers: list[int], index_1: int, index_2: int) -> int:
    index_1 = index_1 if index_1 >= 0 else 0
    index_2 = index_2 if index_2 <= len(numbers) else len(numbers)
    result = 0
    for i in numbers[index_1:index_2]:
        result += i
    return result
