class Animal:
    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type

    def get_unic_attr(self):
        temp = ()
        for k, v in self.__dict__.items():
            if k not in ("_name", "_animal_type"):
                temp += (k, v)
        print(temp)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def animal_type(self) -> str:
        return self._animal_type

    @animal_type.setter
    def animal_type(self, animal_type: str):
        self._animal_type = animal_type

    def __str__(self):
        return  str(self.__dict__)


class Cat(Animal):
    def __init__(self, wild: bool, *args):
        super(Cat, self).__init__(*args)
        self.wild = wild

    @property
    def wild(self) -> bool:
        return self._wild

    @wild.setter
    def wild(self, wild: bool):
        self._wild = wild


class Dog(Animal):
    def __init__(self, *args):
        super(Dog, self).__init__(*args)
        self.commands = []

    @property
    def commands(self) -> list:
        return self._commands

    @commands.setter
    def commands(self, command: (str, list)):
        if isinstance(command, list):
            if command:
                [self._commands.append(i) for i in command]
            else:
                self._commands = []
        elif isinstance(command, str):
            self._commands.append(command)


class Fish(Animal):
    def __init__(self, predator: bool, *args):
        super(Fish, self).__init__(*args)
        self.predator = predator

    @property
    def predator(self) -> bool:
        return self._predator

    @predator.setter
    def predator(self, predator: bool):
        self._predator = predator


if __name__ == '__main__':
    fish = Fish(True, "Sam", "Shark")
    cat = Cat(False, "Barsik", "Pers")
    dog = Dog("Bobik", "Retriver")
    dog.commands = ["сидеть", "служить"]
    fish.get_unic_attr()
    cat.get_unic_attr()
    dog.get_unic_attr()
