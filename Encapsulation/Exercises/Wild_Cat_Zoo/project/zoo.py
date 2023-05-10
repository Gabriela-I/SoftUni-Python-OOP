from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        if self.__animal_capacity != len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity != len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_of_salaries = sum(w.salary for w in self.workers)

        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_money_for_care = sum(a.money_for_care for a in self.animals)

        if self.__budget >= sum_of_money_for_care:
            self.__budget -= sum_of_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        dict_with_animals = {'Lion': [], 'Tiger': [], 'Cheetah': []}
        [dict_with_animals[a.__class__.__name__].append(a) for a in self.animals]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(dict_with_animals['Lion'])} Lions:",
            *dict_with_animals['Lion'],
            f"----- {len(dict_with_animals['Tiger'])} Tigers:",
            *dict_with_animals['Tiger'],
            f"----- {len(dict_with_animals['Cheetah'])} Cheetahs:",
            *dict_with_animals['Cheetah']
        ]

        return '\n'.join([str(x) for x in result])

    def workers_status(self):
        dict_with_workers = {'Keeper': [], '': [], 'Caretaker': [], 'Vet': []}
        [dict_with_workers[w.__class__.__name__].append(w) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(dict_with_workers['Keeper'])} Keepers:",
            *dict_with_workers['Keeper'],
            f"----- {len(dict_with_workers['Caretaker'])} Caretakers:",
            *dict_with_workers['Caretaker'],
            f"----- {len(dict_with_workers['Vet'])} Vets:",
            *dict_with_workers['Vet'],
        ]

        return '\n'.join([str(x) for x in result])


