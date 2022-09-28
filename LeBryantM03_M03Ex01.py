class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around.'


class Midnight(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Susie(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Caramel(Cat):
    def sing(self, sounds):
        return f'{sounds}'


my_cats = [Midnight('Midnight', 3), Susie('Susie', 16), Caramel('Caramel', 7)]

my_pets = Pets(my_cats)

my_pets.walk()
