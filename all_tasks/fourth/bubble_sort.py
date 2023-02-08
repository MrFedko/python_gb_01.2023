def bubble_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for _ in range(length):
        for j in range(length - 1):
            if numbers[j + 1] < numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
