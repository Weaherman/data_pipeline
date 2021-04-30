from pathlib import Path
from typing import List, Dict, NoReturn, Tuple, Any, Generator

print('Path: ', Path(__file__).resolve().parent.parent)
print("Path: ", Path(__file__).resolve().parent)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


#  ETL: Extract, Transform, Load
def read_data(file_name: str) -> Generator:
    """grosse datei einlesen"""
    with open(DATA_DIR / file_name) as f:
        for line in f:
            yield line   #  Generator erstellt
#            print(line)
#        content = f.read()
#        print(content)

def split_line(g: Generator) -> Generator:
#    result = []   # Hilfsmittel zur Ausgabe: was sehe ich hier. sonst funktionslos
    result = (line.strip().split(',') for line in g)   #  HIER kann eine IF Bedingung eingebaut werden zum Screenen der Daten
    return result
    """
    alternativ geht auch:
    for line in g:
        yield line.strip().split(",")
    """


def dictify(g: Generator):
    header = next(g)
    return (dict(zip(header, line)) for line in g)


def load_data(file_name: str) -> Generator:
    file_generator = read_data(file_name)
    split_lines = split_line(file_generator)
    g = read_data(file_name)
    print(next(file_generator))  # ist der Header, 1. Zeile

load_data('techcrunch.csv')

if __name__ == '__main__':
    read_data('techcrunch.csv')


    #      [] {} < > \