import random
from datetime import datetime, timedelta


def collect(sheets):
    today = []
    for sheet in sheets:
        if sheet.get_date() is None or sheet.get_date() <= datetime.today().date():
            today.append(sheet)
    random.shuffle(today)
    return today


def schedule(sheet, confidence):
    next_date = datetime.today().date() + timedelta(
        days={"e": 10, "n": 5, "h": 1}[confidence]
    )
    sheet.set_date(next_date)
