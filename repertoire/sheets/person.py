from .sheet import Sheet


class Person(Sheet):
    def __init__(self, person):
        self.person = person
        super().__init__()

    def get_date(self):
        return self.person.get("next")

    def set_date(self, date):
        self.person["next"] = date

    def print_front(self, printwrap):
        printwrap(self.person["name"])

    def print_back(self, printwrap):
        if "dates" in self.person:
            printwrap(self.person["dates"])
        if "topics" in self.person:
            printwrap(self.person["topics"])
