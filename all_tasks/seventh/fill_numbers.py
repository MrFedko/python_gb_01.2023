from pathlib import Path
from random import randint, uniform


MIN_NUM = -1000
MAX_NUM = 1000


def fill_numbers(count: int, file: str|Path):
    with open(file, 'a', encoding="utf-8") as f:
        for _ in range(count):
            f.write(f'{randint(MIN_NUM, MAX_NUM)}|{uniform(MIN_NUM, MAX_NUM)}\n')
