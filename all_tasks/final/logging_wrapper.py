import logging
from typing import Callable

logging.basicConfig(level=logging.INFO, filename='logs.log', encoding='utf-8')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):

    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dct['result'] = result
        logger.info(dct)

        return result
    return wrapper


@deco_func
def any_name(num: int, *args, **kwargs):
    return num ** 2


if __name__ == '__main__':
    any_name(10, 42, 'Hello', name='Stanislav', x=3, y=True)
