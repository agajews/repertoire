from .sheet import Sheet


class Quote(Sheet):
    def __init__(self, work, quote):
        self.work = work
        self.quote = quote
        super().__init__(quote)

    def print_front(self, printwrap):
        printwrap(self.quote["quote"])

    def print_back(self, printwrap):
        back = "-- "
        if "title" in self.work:
            back += self.work["title"] + "; "
        if "author" in self.work:
            back += self.work["author"] + " "
        if "date" in self.work:
            back += "(" + str(self.work["date"]) + ")"
        printwrap(back)
