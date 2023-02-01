def is_prime(number: int):
    if number & 1 == 0:
        return number == 2
    step = 3
    while step * step <= number and number % step != 0:
        step += 2
    return step * step > number
