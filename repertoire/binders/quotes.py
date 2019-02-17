from ..sheets import Quote
from .binder import Binder


class Quotes(Binder):
    def __init__(self, data):
        self.data = data
        self.sheets = []
        for work in data:
            assert "quotes" in work, "Missing quotes for `{}`".format(repr(work))
            for quote in work["quotes"]:
                assert "quote" in quote, "Missing quote for `{}`".format(repr(work))
                self.sheets.append(Quote(work, quote))
