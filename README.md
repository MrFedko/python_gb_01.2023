# Серия семинаров по python.

## 1. Основы Python [main test](all_tasks/first/main.py)

- Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c -
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним. [code of triangle class](all_tasks/first/triangle.py)
- Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и
на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. 
[code of prime or composite number](all_tasks/first/prime_or_composite.py)
- Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
подсказывать “больше” или “меньше” после каждой попытки.
[code of game like as a binary search](all_tasks/first/binary_search.py)


## 2. Простые типы данных [main test](all_tasks/second/main.py)

- Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление. 
[code](all_tasks/second/num_from_user.py)
- Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. 
Диаметр не превышает 1000. Точность вычисление должна быть не менее 42 знаков после запятой.
[code](all_tasks/second/circle.py)
- напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
[code](all_tasks/second/negative_discr.py)
- Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата. [code](all_tasks/second/hex_number.py)
- Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
[code](all_tasks/second/fractions_from_user.py)


## 3. Коллекции [main test](all_tasks/third/main.py)

- Создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные 
элементы исходного списка.[code](all_tasks/third/uniq_list.py)
- Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов: 
  - целое положительное число;
  - вещественное положительное или отрицательное число;
  - строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква;
  - троку в нижнем регистре в остальных случаях;
  - [code](all_tasks/third/string_from_user.py)
- Создайте вручную кортеж с элементами разных типов. Получите из него словарь списков, где
  - ключ - тип элемента;
  - значение - список элементов данного типа;
  - [code](all_tasks/third/type_dict.py)
- Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, 
встречающиеся дважды. [code](all_tasks/third/double_count.py)
- Создайте вручную список с повторяющимися целыми числами. Сформируйте список с порядковыми номерами нечётных 
элементов исходного списка. Нумерация начинается с единицы. [code](all_tasks/third/odd_index.py)
- Пользователь вводит строку текста. Выведите каждое слово с новой строки.
  - Строки нумеруются с единицы;
  - Слова выводятся отсортированными согласно кодировке Unicode;
  - Текст выравнивается по правому краю, так чтобы у самого длинного слова был один пробел между ним и номером строки.
  - [code](all_tasks/third/nums_of_words.py)
- Пользователь вводит строку. Подсчитайте сколько раз встречается каждая буква в строке. 
Результат сохраните в словарь. [code](all_tasks/third/chr_dict.py)
- Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов. [code](all_tasks/third/only_double.py)
- В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки 
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
[code](all_tasks/third/ten_most_popular.py)
- Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи 
влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака. [code](all_tasks/third/backpack.py)

## 4. Функции [main test](all_tasks/fourth/main.py)

- Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого символа 
введённой строки, отсортированный по убыванию. [code](all_tasks/fourth/uni_code.py)
- Функция получает на вход строку из двух чисел через пробел. Сформируйте словарь, где ключом будет символ из Unicode, а
значением - целое число. Диапазон пар ключ-значение от наименьшего из введенных пользователем до наибольшего 
включительно.[code](all_tasks/fourth/dict_char_num.py)
- Функция получает на вход список чисел. Отсортируйте его элементы in place без использования встроенных в язык 
сортировок. Например, пузырьковая сортировка. [code](all_tasks/fourth/bubble_sort.py)
- Функция принимает три списка одинаковой длинны. (имена (str), ставка(int), процент премии(str вида "10.25%"))
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка 
умноженная на процент премии. [code](all_tasks/fourth/premium.py)
- Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между этими индексами. Если индекс выходит 
за пределы списка, считать от конца и/или начала. [code](all_tasks/fourth/list_sum.py)

## 5. Итераторы и генераторы [main test](all_tasks/fifth/main.py)

- Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
  - второе и третье число являются ключами.
  - первое число является значением для первого ключа.
  - четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа
  [code](all_tasks/fifth/dict_with_int.py)
- Самостоятельно сохраните в переменной строку текста. Создайте из строки словарь, где ключ — буква, а значение — код 
буквы. Напишите преобразование в одну строку. [code](all_tasks/fifth/dict_chr_ord.py) 
- Продолжаем развивать задачу 2.
  - Возьмите словарь, который вы получили.
Сохраните его итератор.
  - Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю. [code](all_tasks/fifth/main.py) (15-16 строки)
- Создайте генератор чётных чисел от нуля до 100.
  - Из последовательности исключите
числа, сумма цифр которых равна 8.
  - Решение в одну строку. [code](all_tasks/fifth/main.py) (20 строка)
- Напишите программу, которая выводит
на экран числа от 1 до 100.
  - При этом вместо чисел, кратных трем,
  программа должна выводить слово «Fizz»
  - Вместо чисел, кратных пяти — слово «Buzz».
  - Если число кратно и 3, и 5, то программа
  должна выводить слово «FizzBuzz».
  - *Превратите решение в генераторное выражение.
  [code](all_tasks/fifth/fizz_buzz.py)
- Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
  - Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
  - Для вывода результата используйте «принт»
без перехода на новую строку.
  [code](all_tasks/fifth/product_table.py)
- Создайте функцию-генератор.
  - Функция генерирует N простых чисел,
начиная с числа 2.
  - Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу 
  и на себя». [code](all_tasks/fifth/prime_gen.py)
- Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла. [code](all_tasks/fifth/file_path.py)
- Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии. [code](all_tasks/fourth/premium.py)
- Создайте функцию генератор чисел Фибоначчи. [code](all_tasks/fifth/fibo.py)

## 6. Модули [main test](all_tasks/sixth/main.py)

- Вспомните какие модули вы уже проходили на курсе.
  - Создайте файл, в котором вы импортируете встроенные
в модуль функции под псевдонимами. (3-7 строк импорта). [code](all_tasks/sixth/import.py)
  
- Создайте модуль с функцией внутри.
  - Функция принимает на вход три целых числа:
нижнюю и верхнюю границу и количество попыток.
  - Внутри генерируется случайное число в указанных
границах и пользователь должен угадать его за
заданное число попыток.
  - Функция выводит подсказки «больше» и «меньше».
  - Если число угадано, возвращается истина,
а если попытки исчерпаны — ложь. [code](all_tasks/sixth/binary_random_search.py)

- Улучшаем задачу 2.
  - Добавьте возможность запуска функции «угадайки»
из модуля в командной строке терминала.
  - Строка должна принимать от 1 до 3 аргументов:
параметры вызова функции.
  - Для преобразования строковых аргументов
командной строки в числовые параметры
используйте генераторное выражение. [code](all_tasks/sixth/search_script.py)

- Создайте модуль с функцией внутри.
  - Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
  - Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны. [code](all_tasks/sixth/one_hundred_for_one.py) (10-18 строки)

- Добавьте в модуль с загадками функцию, которая хранит словарь списков.
  - Ключ словаря — загадка, значение — список с отгадками.
  - Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 
  [code](all_tasks/sixth/one_hundred_for_one.py)
