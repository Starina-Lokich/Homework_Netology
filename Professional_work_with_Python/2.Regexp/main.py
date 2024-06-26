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
        

def correct_phone_number(data_list: list) -> list:
    """
    Приводит все телефоны в формат +7(999)999-99-99 или +7(999)999-99-99 доб.9999
    """
    new_contacts_list = []

    pattern = re.compile(r'([А-Я]\w+)\,([А-Я]\w+)\,([А-Я]\w+)\,([А-Я]\w+)\,?(\D+)?\,\+?(\d{1})\s?\W?(\d{3})'
                         r'\W*(\d{3})\W?(\d{2})\W?(\d{2})\W*([а-я.]+)?\W?(\d{4})?\)?\,(\S+)?')
    
    for contact in data_list:
        result = pattern.sub(r'\1,\2,\3,\4,\5,+7(\7)\8-\9-\10 \11\12,\13', str(','.join(contact)))
        new_contacts_list.append(result)
    return new_contacts_list


def write_csv(filename: str, encoding: str, data_list: list) -> list:
    """
    Записываем данные из списка в CSV
    """

    with open(filename, 'w', encoding=encoding, newline='') as f:
        datawriter = csv.writer(f, delimiter='\n')
        datawriter.writerows([data_list])




if __name__ == '__main__':
    data_list = read_csv('phonebook_raw.csv', 'UTF-8')# Читаем файл CSV и записываем данные в список
    data_list = correct_full_name(data_list) # Разбиваем ФИО на отдельные элементы списка
    data_list = sorted_data_list(data_list) # Сортируеv и обединяеv фрагменты данных в одно целое. Убираеv дубли
    data_list = correct_phone_number(data_list) # Приводим все телефоны в формат +7(999)999-99-99 или +7(999)999-99-99 доб.9999
    write_csv('phonebook.csv', 'UTF-8', data_list) # Записываем полностью отформатированные список в CSV
