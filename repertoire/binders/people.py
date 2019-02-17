from ..sheets import Person
from .binder import Binder


class People(Binder):
    def __init__(self, data):
        self.data = data
        self.sheets = []
        for person in data:
            assert "name" in person, "Missing name: {}".format(person)
            self.sheets.append(Person(person))
