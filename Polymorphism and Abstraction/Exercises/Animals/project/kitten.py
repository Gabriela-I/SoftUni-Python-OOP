from project.cat import Cat


class Kitten(Cat):
    GENDER = 'Female'

    def __init__(self, name, age): #(self, name, age, gender='Female'
        super().__init__(name, age, Kitten.GENDER)

    def make_sound(self):
        return 'Meow'


