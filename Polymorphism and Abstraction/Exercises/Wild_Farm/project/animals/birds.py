from project.animals.animal import Bird
from project.food import Meat, Fruit, Seed, Vegetable


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def food_that_eats(self):
        return [Meat]

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def gained_weight(self):
        return 0.35

    @property
    def food_that_eats(self):
        return [Vegetable, Seed, Fruit, Meat]


