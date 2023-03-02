from animals import Cat, Dog, Fish


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"dog": Dog, "cat": Cat, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Bobik", "Retriver")
    animal_from_fabric.commands = ["сидеть", "служить"]
    print(animal_from_fabric)
