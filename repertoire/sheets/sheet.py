class Sheet:
    def __init__(self, data):
        self._data = data

    @property
    def date(self):
        return self._data.get("next")

    @date.setter
    def date(self, date):
        self._data["next"] = date

    @property
    def interval(self):
        return self._data.get("interval", 1)

    @interval.setter
    def interval(self, interval):
        self._data["interval"] = interval

    def print_front(self, printwrap):
        raise NotImplementedError()

    def print_back(self, printwrap):
        raise NotImplementedError()
