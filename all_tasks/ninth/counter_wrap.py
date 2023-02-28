from typing import Callable


def counter_wrap(count: int):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco


@counter_wrap(5)
def testing(count: int):
    print("test")


if __name__ == '__main__':
    testing(4)
