from .sheet import Sheet
from ..latex import get_latex_image, print_image


class MathSheet(Sheet):
    def __init__(self, sheet):
        self.sheet = sheet
        self.latex_image = None
        super().__init__()

    def get_date(self):
        return self.sheet.get("next")

    def set_date(self, date):
        self.sheet["next"] = date

    def print_front(self, printwrap):
        printwrap(self.sheet["name"])
        latex = self.sheet["statement"]
        if "proof" in self.sheet:
            latex += r"\begin{proof}" + self.sheet["proof"] + r"\end{proof}"
        self.latex_image = get_latex_image(latex)
        print()

    def print_back(self, printwrap):
        print_image(self.latex_image)
        return ""
