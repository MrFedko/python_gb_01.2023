class People:
    def __init__(self, name: str, surname, age: int):
        self.name = name
        self.surname = surname
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        self._surname = surname

    @property
    def age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        print(f"{self.name} {self.surname}")


if __name__ == '__main__':
    mikle = People("Mikle", "Smith", 31)
    mikle.birthday()
    mikle.birthday()
    print(mikle.age)
    mikle.full_name()
