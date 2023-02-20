from random import choices, randint
from string import ascii_letters, digits


def make_files(extension: str, min_name: int = 6, max_name: int = 30,
            min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters+digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

