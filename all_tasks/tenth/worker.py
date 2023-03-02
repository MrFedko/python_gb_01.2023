import random
from people import People


class Worker(People):
    __workers_id =[]

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.__worker_id = None
        self.__secure_lvl = None

    @property
    def worker_id(self) -> int:
        if self.__worker_id is None:
            temp = random.randint(100000, 999999)
            while temp in Worker.__workers_id:
                temp = random.randint(100000, 999999)
            self.__worker_id = temp
            Worker.__workers_id.append(temp)
        return self.__worker_id

    @property
    def secure_lvl(self) -> int:
        if self.__secure_lvl is None:
            temp = sum((int(i) for i in str(self.worker_id))) % 7
            self.__secure_lvl = temp
        return self.__secure_lvl


if __name__ == '__main__':
    mikle = Worker("Mikle", "Smith", 31)
    mikle.birthday()
    mikle.birthday()
    print(mikle.age)
    mikle.full_name()
    print(mikle.worker_id)
    print(mikle.secure_lvl)
