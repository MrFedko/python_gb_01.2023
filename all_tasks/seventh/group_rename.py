import os
from pathlib import Path


def group_rename(count_len: int, extension: str, new_extension: str, interval: list[int], new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}")
