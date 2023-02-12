from dict_with_int import dict_with_int
from dict_chr_ord import dict_chr_ord
from fizz_buzz import fizz_buzz
from product_table import product_table
from prime_gen import prime_gen
from file_path import file_info
from premium import premium
from fibo import fibo

if __name__ == "__main__":
    # dict with int
    print(dict_with_int(input("Введите от 4 чисел разделенных символом / ")))

    print("*" * 50)

    text = "Это текст для тестирования функции, где ключ - символ, а значение - его код."
    print(dict_chr_ord(text))

    print("*" * 50)

    my_dict = iter(dict_chr_ord(text).items())
    [print(next(my_dict)) for _ in range(5)]

    print("*" * 50)

    print([i for i in range(0, 101, 2) if i // 10 + i % 10 != 8])

    print("*" * 50)

    print(*fizz_buzz())

    print("*" * 50)

    product_table()

    print("*" * 50)

    [print(i, end=" ") for i in prime_gen(int(input("Сколько простых чисел вывести? ")))]

    print("*" * 50)

    file_p = "/Users/mac/Desktop/GeekBrain/second_python/README.md"
    print(file_info(file_p))

    print("*" * 50)

    # return dict with premium
    names = ["John", "Bill", "Liz"]
    cash = [123, 321, 432]
    percent = ["10.25%", "55.05%", "33.75%"]
    print(premium(names, cash, percent))

    print("*" * 50)

    # fibo nums
    [print(i, end=" ") for i in fibo(int(input("Сколько чисел Фибоначчи вывести на экран? ")))]
