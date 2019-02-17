class Sheet:
    def get_date(self):
        raise NotImplementedError()

    def set_date(self, date):
        raise NotImplementedError()

    def print_front(self, printwrap):
        raise NotImplementedError()

    def print_back(self, printwrap):
        raise NotImplementedError()
