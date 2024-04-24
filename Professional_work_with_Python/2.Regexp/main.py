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


def sorted_data_list(data_list: list) -> list:
    """
    Сортирует и обединяет фрагменты данных в одно целое. Убирает дубли
    """

    for contact_1 in data_list:
        for contact_2 in data_list[1:]:
            if contact_1[4] == '':
                if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1] and contact_2[4] != '':
                    contact_1[4] = contact_2[4]
                    data_list.remove(contact_2)
            if contact_1[6] == '':
                if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1] and contact_2[6] != '':
                    contact_1[6] = contact_2[6]
                    data_list.remove(contact_2)
    return data_list
        
