from dict_with_int import dict_with_int
from dict_chr_ord import dict_chr_ord
from fizz_buzz import fizz_buzz

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
