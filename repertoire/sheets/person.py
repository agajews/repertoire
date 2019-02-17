from .sheet import Sheet


class Person(Sheet):
    def __init__(self, person):
        self.person = person
        super().__init__(person)

    def print_front(self, printwrap):
        printwrap(self.person["name"])

    def print_back(self, printwrap):
        if "dates" in self.person:
            printwrap(self.person["dates"])
        if "topics" in self.person:
            printwrap(self.person["topics"])
