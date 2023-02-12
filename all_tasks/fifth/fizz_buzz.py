def fizz_buzz() -> iter:
    return ('FizzBuzz' if num % 3 == 0 and num % 5 == 0
                else 'Fizz' if num % 3 == 0
                else 'Buzz' if num % 5 == 0
                else num for num in range(1, 101))
