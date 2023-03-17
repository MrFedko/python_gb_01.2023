import argparse
from datetime import datetime

from date_from_text import get_date, WEEKDAYS, MONTHS


def parser_func():
    parser = argparse.ArgumentParser(description='Получаем дату datetime из строки')
    parser.add_argument('--count', default='1')
    parser.add_argument('--weekday', default=datetime.now().weekday())
    parser.add_argument('--month', default=datetime.now().month)
    args = parser.parse_args()
    print(args)
    weekday = WEEKDAYS[args.weekday] if isinstance(args.weekday, int) else args.weekday
    month = MONTHS[args.month] if isinstance(args.month, int) else args.month
    return get_date(f'{args.count} {weekday} {month}')


if __name__ == '__main__':
    print(parser_func())
