documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    result = "Документ не найден"
    for document in documents:
        for key, value in document.items():
            if doc_number == document["number"]:
                result = document["name"]
                break
    return result


def get_directory(doc_number):
    result = "Полки с таким документом не найдено"
    for shelf, document in directories.items():
        if doc_number in document:
            result = shelf
            break
    return result


def add(document_type, number, name, shelf_number):
    documents.append({"type": document_type, "number": number, "name": name})
    if shelf_number in directories:
        directories[str(shelf_number)].append(number)
    else:
        directories[str(shelf_number)] = [number]
    return documents, directories
    









# def test_add(document_type, number, name, shelf_number):
#     result = add(document_type, number, name, shelf_number)
#     assert document_type in documents[-1]["type"]
#     assert number in documents[-1]["number"]
#     assert name in documents[-1]["name"] 
#     assert str(shelf_number) in directories
#     assert number in directories[str(shelf_number)]

# test_add('international passport', '311 020203', 'Александр Пушкин', 3)


# if __name__ == '__main__':
#     print(get_name("10006"))
#     print(get_directory("11-2"))
#     print(get_name("101"))
#     add('international passport', '311 020203', 'Александр Пушкин', 3)
#     print(get_directory("311 020203"))
#     print(get_name("311 020203"))
#     print(get_directory("311 020204"))
