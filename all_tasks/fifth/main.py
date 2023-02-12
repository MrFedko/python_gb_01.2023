from dict_with_int import dict_with_int
from dict_chr_ord import dict_chr_ord

if __name__ == "__main__":
    # dict with int
    print(dict_with_int(input("Введите от 4 чисел разделенных символом / ")))

    print("*" * 50)

    text = "Это текст для тестирования функции, где ключ - символ, а значение - его код."
    print(dict_chr_ord(text))
