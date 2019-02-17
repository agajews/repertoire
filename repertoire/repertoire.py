# import sys
import textwrap

import click
from getkey import getkey
from ruamel.yaml import YAML

from .binders import binders
from .scheduler import Scheduler
from .term import term

yaml = YAML()


def read(name):
    if not name.endswith(".yaml"):
        name += ".yaml"
    with open(name, "r") as f:
        # try:
        data = yaml.load(f)
        # except yaml.scanner.ScannerError as e:
        #     print("=" * 30 + " Failed to read file " + "=" * 30)
        #     print(e)
        #     sys.exit(1)
    assert "binder" in data, "Missing binder"
    assert data["binder"] in binders, "Invalid binder"
    assert "sheets" in data, "Missing sheets"
    # print(data)
    binder = binders[data["binder"]](data["sheets"])
    return data, binder


def write(name, data):
    if not name.endswith(".yaml"):
        name += ".yaml"
    with open(name, "w") as f:
        yaml.dump(data, f)


@click.group()
def cli():
    pass


def getnum():
    key = getkey()
    while key not in "renh":
        key = getkey()
    return key


def printwrap(text, centery=False):
    width = 3 * term.width // 5
    lines = []
    for line in text.split("\n"):
        lines += textwrap.wrap(line, width)
    if centery:
        print(term.move((term.height - len(lines)) // 2 - 2, 0))
    for line in lines:
        print(line.center(term.width))


@cli.command()
@click.argument("name")
def rehearse(name):
    data, binder = read(name)
    scheduler = Scheduler(binder.sheets)

    with term.fullscreen():
        while scheduler.today:
            sheet = scheduler.today.pop()
            sheet.print_front(lambda text: printwrap(text, centery=True))
            getkey()
            sheet.print_back(lambda text: printwrap(text, centery=False))
            confidence = getnum()
            scheduler.schedule(sheet, confidence)
            print(term.clear())

    write(name, data)
    print("All done for today :D")


if __name__ == "__main__":
    cli()
