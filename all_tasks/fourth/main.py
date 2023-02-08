from uni_code import uni_code
from dict_char_num import dict_char_num
from bubble_sort import bubble_sort


if __name__ == "__main__":
    # set of chars to unicode with sort
    text = "Функция ord() для символа x вернет число, из таблицы символов Unicode представляющее его позицию. Например, " \
           "ord('a') возвращает целое число 97 и ord('€') вернет 8364. Функция ord() обратная chr(). Для символа " \
           "строки 8-бит возвращает значение байта. Если передан символов Unicode и Python собран с UCS2 Unicode, " \
           "то позиция кода должна находиться в диапазоне от 0 до 65535 включительно, иначе возбуждается исключение " \
           "TypeError."

    print([f"{i} {chr(i)}" for i in uni_code(text)])

    # dict with chars and nums
    print(dict_char_num(input("введите два числа через пробел: ")))

    # bubble sort
    numbers = [1, 3, 5, 7, 2, 8, 10, 142, 23, 45, 6, 3, 2, 5]
    print(bubble_sort(numbers))
