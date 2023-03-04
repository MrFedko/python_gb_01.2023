from time import time


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance


if __name__ == '__main__':
    s = MyStr('hello', 'qwerty')
    print(s)
    print(s.author)
    s2 = MyStr('si', 'asdfg')
    print(s2.author)
    print(s.upper())
    print(s.time, s2.time)
