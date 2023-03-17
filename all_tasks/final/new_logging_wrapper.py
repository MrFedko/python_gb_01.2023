import logging
from functools import wraps
from typing import Callable

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='logs.log', encoding='utf-8',
format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        # print(func.__name__)
        # dct['result'] = result
        logger.info(f'func: {func.__name__} - {dct} - "result": {result}')

        return result
    return wrapper


@deco_func
def any_name(num: int, *args, **kwargs):
    return num ** 2


if __name__ == '__main__':
    any_name(10, 42, 'Hello', name='Stanislav', x=3, y=True)
