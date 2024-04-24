import csv
import re


def read_csv(filename: str, encoding: str) -> list:
    """
    Прочитывает данные CSV и записывает их с список
    """

    with open(filename, "r", encoding=encoding) as csv_file: 
        return list(csv.reader(csv_file))
    

def correct_full_name(data_list: list) -> list:
    """
    Разбивает ФИО на отдельные элементы списка

    Пример работы:
    ['Усольцев Олег Валентинович'] -> ['Усольцев', 'Олег', 'Валентинович']
    ['Усольцев', 'Олег Валентинович'] -> ['Усольцев', 'Олег', 'Валентинович']
    """

    for contacts in data_list:
        if len(contacts[0].split()) > 2:
            contacts[1] = contacts[0].split()[1]
            contacts[2] = contacts[0].split()[2]
            contacts[0] = contacts[0].split()[0]
        elif len(contacts[1].split()) > 1:
            contacts[2] = contacts[1].split()[1]
            contacts[1] = contacts[1].split()[0]
        elif len(contacts[0].split()) == 2:
            contacts[1] = contacts[0].split()[1]
            contacts[0] = contacts[0].split()[0]
    return data_list

