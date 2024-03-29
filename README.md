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

- Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
  - Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
  - Для простоты договоримся, что год может быть в диапазоне [1, 9999].
  - Весь период (1 января 1 года — 31 декабря 9999 года) действует Григорианский календарь.
  - Проверку года на високосность вынести в отдельную защищённую функцию. [code](all_tasks/sixth/date_validate.py)

- В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
[code](all_tasks/sixth/date_validate.py)

- Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей 
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое 
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. 
[code](all_tasks/sixth/ferzi.py)

- Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче 
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки. [code](all_tasks/sixth/ferzi.py)


## 7. Файловая система [main test](all_tasks/seventh/main.py)

- Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
   - Первое число int, второе - float разделены вертикальной чертой.
   - Минимальное число - -1000, максимальное - +1000.
   - Количество строк и имя файла передаются как аргументы функции. 
[code](all_tasks/seventh/fill_numbers.py)


- Напишите функцию, которая генерирует псевдоимена.
  - Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
  - Полученные имена сохраните в файл. [code](all_tasks/seventh/name_gen.py)


- Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
  - Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
  - если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
  - если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
  - В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
  - При достижении конца более короткого файла,
возвращайтесь в его начало. [code](all_tasks/seventh/from_two_files.py)


- Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
  - расширение
  - минимальная длина случайно сгенерированного имени, по умолчанию 6
  - максимальная длина случайно сгенерированного имени, по умолчанию 30
  - минимальное число случайных байт, записанных в файл, по умолчанию 256
  - максимальное число случайных байт, записанных в файл, по умолчанию 4096
  - количество файлов, по умолчанию 42
  - Имя файла и его размер должны быть в рамках переданного диапазона.
[code](all_tasks/seventh/make_files.py)

  
- Доработаем предыдущую задачу.
  Создайте новую функцию которая генерирует файлы с разными расширениями.
  - Расширения и количество файлов функция принимает в качестве параметров.
  - Количество переданных расширений может быть любым.
  - Количество файлов для каждого расширения различно.
  - Внутри используйте вызов функции из прошлой задачи.
  [code](all_tasks/seventh/new_make_files.py)


- Напишите функцию группового переименования файлов. Она должна:
   - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
   - принимать параметр количество цифр в порядковом номере.
   - принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
   - принимать параметр расширение конечного файла.
   - принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
  [code](all_tasks/seventh/group_rename.py)


## 8. Сериализация

- Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
  - Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
  - Имена пишите с большой буквы.
  - Каждую пару сохраняйте с новой строки.
  [code](all_tasks/eights/txt_to_json.py)


- Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
  - После каждого ввода добавляйте новую информацию в JSON файл.
  - Пользователи группируются по уровню доступа.
  - Идентификатор пользователя выступает ключём для имени.
  - Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
  - При перезапуске функции уже записанные в файл данные должны сохраняться.
  [code](all_tasks/eights/get_from_user.py)


- Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV. 
[code](all_tasks/eights/json_to_csv.py)


- Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
  - Дополните id до 10 цифр незначащими нулями.
  - В именах первую букву сделайте прописной.
  - Добавьте поле хеш на основе имени и идентификатора.
  - Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
  - Имя исходного и конечного файлов передавайте как аргументы функции.
  [code](all_tasks/eights/csv_to_json.py)


- Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
  - Для дочерних объектов указывайте родительскую директорию.
  - Для каждого объекта укажите файл это или директория.
  - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и 
  директорий.
  - Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
  [code](all_tasks/eights/direct_info.json)


## 9. Декораторы


- Создайте функцию-замыкание, которая запрашивает два целых числа:
  - от 1 до 100 для загадывания,
  - от 1 до 10 для количества попыток
  - Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
  [code](all_tasks/ninth/binary_search_game.py)


- Дорабатываем задачу 1.
  - Превратите внешнюю функцию в декоратор.
  - Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
  - Если не входят, вызывать функцию со случайными числами из диапазонов.
  [code](all_tasks/ninth/binary_search_game_wrap.py)


- Создайте декоратор с параметром. 
 Параметр - целое число, количество запусков декорируемой функции. [code](all_tasks/ninth/counter_wrap.py)


- Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. 
При повторном вызове файл должен расширяться, а не перезаписываться.
  - Каждый ключевой параметр сохраните как отдельный ключ json словаря.
  - Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
  - Имя файла должно совпадать с именем декорируемой функции.


- Объедините функции из прошлых задач.
  Функцию угадайку задекорируйте:
   - декораторами для сохранения параметров
   - декоратором контроля значений
   - декоратором для многократного запуска
- Выберите верный порядок декораторов.
[code](all_tasks/ninth/binary_search_game_wrap.py)


- Напишите следующие функции:
  - Нахождение корней квадратного уравнения
  - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
  - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
  - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
  - Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
  [code](all_tasks/ninth/final.py)


## 10. ООП. Начало


 - Создайте класс окружность. Класс должен принимать радиус окружности при создании.
У класса должно быть два метода, возвращающие длину окружности и ее площадь. [code](all_tasks/tenth/circle.py)


 - Создайте класс прямоугольник. 
    - Класс должен принимать длину и ширину при создании экземпляра.
    - У класса должно быть два метода, возвращающие периметр и площадь.
    - Если при создании передается только одна сторона, считаем что у нас квадрат.
   [code](all_tasks/tenth/rectangle.py)


- Напишите класс для хранения информации о человеке. ФИО, возраст и т.п. на выбор.
  - У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО.
  - Убедитесь что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст. 
[code](all_tasks/tenth/people.py)


- Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания.
 У сотрудника должен быть:
  - шестизначный идентификационный номер
  - уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь.
[code](all_tasks/tenth/worker.py)


- Создайте три класса животных. 
  - У каждого класса должны быть как общие свойства, так и специфичные для класса.
  - Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
[code](all_tasks/tenth/animals.py)


- Доработаем задачи 5-6. 
Создайте класс-фабрику. 
  - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
  - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
[code](all_tasks/tenth/animal_fabric.py)


## 11. ООП. Особенности Python

- Создайте класс Моя Строка, где:
  - будут доступны все возможности str
  - дополнительно хранятся имя автора строки и время создания (time.time)
  [code](all_tasks/eleventh/my_string.py)


- Создайте класс Архив, который хранит пару свойств. Например, число и строку.
  - При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
  - list-архивы также являются свойствами экземпляра
  [code](all_tasks/eleventh/archiv.py)


- Доработаем класс Архив из задачи 2.
  - Добавьте методы представления экземпляра для программиста и для пользователя.
  [code](all_tasks/eleventh/archiv.py)


- Дорабатываем класс прямоугольник из прошлого семинара.
  - Добавьте возможность сложения и вычитания.
  - При этом должен создаваться новый экземпляр прямоугольника.
  - Складываем и вычитаем периметры, а не длину и ширину.
  - При вычитании не допускайте отрицательных значений.
  [code](all_tasks/eleventh/rectangle.py)

- Доработайте прошлую задачу.
  - Добавьте сравнение прямоугольников по площади
  - Должны работать все шесть операций сравнения
  [code](all_tasks/eleventh/rectangle.py)


- Создайте класс Матрица. Добавьте методы для:
  - вывода на печать
  - сравнения
  - сложения
  - *умножения матриц [code](all_tasks/eleventh/matrix.py)


## 12. ООП. Финал


 - Создайте класс студента.
    - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре 
   недопустимы.
    - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе 
   взятых.
   [code](all_tasks/twelfth/student.py)


## 13. Исключения

- Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
  - Напишите к ним классы исключения с выводом подробной информации.
  - Поднимайте исключения внутри основного кода.
    [code](all_tasks/exeptions/user_exceptions.py)


## 14. Основы тестирования

 - Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
    - Напишите к ним тесты.
    - 2-5 тестов на задачу в трёх вариантах:
       - doctest,
       - unittest,
       - pytest.
      
    [code](all_tasks/testing/my_func.py)


##  15. Обзор стандартной библиотеки Python

- Напишите программу, которая использует модуль logging для вывода сообщений об ошибке в файл.
[code](all_tasks/final/logging_error.py)


- На семинаре про декораторы был создан логирующий декоратор. Он охранял аргументы функции и ее результат в файл.
Напишите аналогичный декоратор, использующий модуль logging.
[code](all_tasks/final/logging_wrapper.py)


- Доработаем задачу 2. Сохраняйте в лог раздельно:
    - уровень логирования
    - дату события
    - имя функции
    - аргументы вызова
    - результат
  [code](all_tasks/final/new_logging_wrapper.py)


- Функция принимает на вход текст типа "1-й четверг ноября"
  - Преобразуйте его в дату в текущем году
  - Логируйте ошибки, если текст не соответствует формату.
  [code](all_tasks/final/date_from_text.py)


- Дорабатываем задачу 4.
    - добавьте возможность запуска из командной строки.
    - при это значение любого параметра можно опустить. При этом берется первый в месяце день недели, текущий день и\или
  текущий месяц.
  [code](all_tasks/final/new_date_from_text.py)


- Возьмите любые 1-3 задачи из прошлых домашних заданий. 
    - Добавьте к ним логирование ошибок и полезной информации. 
    - Также реализуйте возможность запуска из командной строки с передачей параметров.
[code](all_tasks/final/my_func.py)
