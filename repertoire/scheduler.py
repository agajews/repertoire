import random
from datetime import datetime, timedelta


class Scheduler:
    def __init__(self, sheets):
        self.today = []
        for sheet in sheets:
            if sheet.date is None or sheet.date <= datetime.today().date():
                self.today.append(sheet)
        random.shuffle(self.today)

    def schedule(self, sheet, confidence):
        if confidence == "r":
            self.today.insert(random.randrange(len(self.today) + 1), sheet)
            sheet.interval = 1
        else:
            factor = {"e": 3, "n": 2, "h": 1}[confidence] * random.uniform(0.9, 1.1)
            sheet.interval = round(sheet.interval * factor, 2)
            sheet.date = datetime.today().date() + timedelta(days=int(sheet.interval))
