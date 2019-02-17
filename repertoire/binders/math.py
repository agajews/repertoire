from ..sheets import MathSheet
from .binder import Binder


class Math(Binder):
    def __init__(self, data):
        self.data = data
        self.sheets = []
        for sheet in data:
            assert "name" in sheet, "Missing name for `{}`".format(repr(sheet))
            assert "statement" in sheet, "Missing statement for `{}`".format(
                repr(sheet)
            )
            self.sheets.append(MathSheet(sheet))
