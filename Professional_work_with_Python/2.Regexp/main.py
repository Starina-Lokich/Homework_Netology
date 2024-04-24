import csv
import re


def read_csv(filename: str, encoding: str) -> list:
    """
    Прочитывает данные CSV и записывает их с список
    """

    with open(filename, "r", encoding=encoding) as csv_file: 
        return list(csv.reader(csv_file))
    
