from random import choice, randint
from pathlib import Path

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def name_gen(count_strings: int, str_len_min: int, str_len_max: int, file_1: Path):
    with open(file_1, 'a', encoding='utf-8') as f_1:
        for _ in range(count_strings):
            rand_string = ''.join(choice(VOWELS) if i % 3 == 0 else choice(CONSONANTS)
                    for i in range(randint(str_len_min, str_len_max)))
            f_1.write(f'{rand_string.capitalize()}\n')


