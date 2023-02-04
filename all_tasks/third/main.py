from uniq_list import uniq
from string_from_user import reformat
from type_dict import get_type_dict
from double_count import double_count
from odd_index import odd_index
from nums_of_words import num_of_words
from chr_dict import chr_dict
from only_double import only_double
from ten_most_popular import ten_popular
from backpack import backpack

if __name__ == "__main__":
    # get uniq numbers
    print(uniq([int(i) for i in input("Введите целые числа через пробел: ").split()]))

    # check type of text
    result = reformat(input("Введите данные: "))
    print(result, type(result))

    # dict of types
    my_tuple = (1, 2, "any", "text", 1.34, 5.23, [1, 2, 3, 4, 5], [2, 3, 4], (1, 2), (3, 4))
    print(get_type_dict(my_tuple))

    # delete double count elements
    my_list = [1, 2, 3, 4, 1, 5, 3, 3]
    print(double_count(my_list))

    # return indexes of odd elements
    #         1  2  3  4  5  6  7  8   9
    my_lst = [2, 4, 6, 8, 3, 5, 7, 10, 5]
    print(odd_index(my_lst))

    # printing text
    text = "Once you’ve written some code that works with Unicode data, the next problem is input/output. How do you " \
           "get Unicode strings into your program, and how do you convert Unicode into a form suitable for storage " \
           "or transmission?"
    num_of_words(text)

    # get dict of chars
    text = "Once you’ve written some code that works with Unicode data, the next problem is input/output. How do you"
    [print(f"{key}: {value}") for key, value in chr_dict(text).items()]

    # return only elements with count() > 1
    my_list = [2, 4, 6, 8, 3, 5, 7, 10, 5]
    print(only_double(my_list))

    # most popular words
    text = "Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно " \
           "используемых платформ и являющийся стандартом де-факто языка. Он распространяется под свободной " \
           "лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых " \
           "приложениях, включая проприетарные. CPython компилирует исходные тексты в высокоуровневый байт-код, " \
           "который исполняется в стековой виртуальной машине. К другим трём основным реализациям языка относятся " \
           "Jython (для JVM), IronPython (для CLR/.NET) и PyPy. PyPy написан на подмножестве языка Python " \
           "(RPython) и разрабатывался как альтернатива CPython с целью повышения скорости исполнения программ, в том " \
           "числе за счёт использования JIT-компиляции. Поддержка версии Python 2 закончилась в 2020 году. " \
           "На текущий момент активно развивается версия языка Python 3. Разработка языка ведётся через " \
           "предложения по расширению языка PEP (англ. Python Enhancement Proposal), в которых описываются " \
           "нововведения, делаются корректировки согласно обратной связи от сообщества и документируются итоговые " \
           "решения. Стандартная библиотека включает большой набор полезных переносимых функций, начиная с " \
           "возможностей для работы с текстом и заканчивая средствами для написания сетевых приложений. Дополнительные " \
           "возможности, такие как математическое моделирование, работа с оборудованием, написание веб-приложений или " \
           "разработка игр, могут реализовываться посредством обширного количества сторонних библиотек, а также " \
           "интеграцией библиотек, написанных на Си или C++, при этом и сам интерпретатор Python может интегрироваться " \
           "в проекты, написанные на этих языках. Существует и специализированный репозиторий программного " \
           "обеспечения, написанного на Python, — PyPI. Данный репозиторий предоставляет средства для простой " \
           "установки пакетов в операционную систему и стал стандартом де-факто для Python. По состоянию на 2019 " \
           "год в нём содержалось более 175 тысяч пакетов. Python стал одним из самых популярных языков, он " \
           "используется в анализе данных, машинном обучении, DevOps и веб-разработке, а также в других сферах, " \
           "включая разработку игр. За счёт читабельности, простого синтаксиса и отсутствия необходимости в компиляции " \
           "язык хорошо подходит для обучения программированию, позволяя концентрироваться на изучении алгоритмов, " \
           "концептов и парадигм. Отладка же и экспериментирование в значительной степени облегчаются тем фактом, что " \
           "язык является интерпретируемым. Применяется язык многими крупными компаниями, такими как Google или " \
           "Facebook. По состоянию на сентябрь 2022 года Python занимает первое место в рейтинге TIOBE популярности " \
           "языков программирования с показателем 15,74%. «Языком года» по версии TIOBE Python объявлялся в 2007, " \
           "2010, 2018, 2020 и 2021 годах."
    print(ten_popular(text))

    # backpack
    shop = {"носки": 1, "штаны": 3, "футболка": 2, "футболка_2": 2, "куртка": 5, "кепка": 1}
    backpack_size = 7
    [print(i) for i in backpack(shop, backpack_size)]
