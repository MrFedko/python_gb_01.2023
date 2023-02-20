from pathlib import Path
from fill_numbers import fill_numbers
from name_gen import name_gen
from from_two_files import from_two_files
from make_files import make_files


if __name__ == '__main__':
    fill_numbers(20, 'numbers.txt')

    name_gen(10, 4, 7, Path('names.txt'))

    from_two_files(Path('numbers.txt'), Path('names.txt'), Path('result.txt'))

    make_files('bin', count=10)
