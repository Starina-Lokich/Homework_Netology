'Задание - Соберите уникальные имена преподавателей'

def get_unique_names(list_people: list[list[staticmethod]]) -> str:
    """
    Приниммает список со списками, в которых храняться ФИ/ФИО преподователей с разных курсов
    
    Возвращает строку с именами преподователей
    """
    name_list = []
    [name_list.append(name.split([0])) for name in sum(list_people, [])]
    unique_names_sort = ', '.join(sorted(set(name_list)))
    return unique_names_sort


'Задание - Узнайте топ-3 популярных имён'

def get_top_3_names(people_list: list[list[str]]) -> str:
    """
    Приниммает список со списками, в которых храняться ФИ/ФИО преподователей с разных курсов
    
    Возвращает строку с 3-мя самыми встречающимися именами среди преподавателей 
    """   
    name_list = []
    [name_list.append(name.split()[0]) for name in sum(people_list, [])]
    name_rating = []
    [name_rating.append([name, name_list.count(name)]) for name in set(name_list)]
    name_rating.sort(key=lambda x:x[1], reverse=True)
    result = ''
    for name, count in name_rating[0:3]:
        result += f'{name}: {count} раз(а), '
    return result[:-2]