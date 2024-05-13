import unittest
from Task_1_unit_tests.secretary import add, get_name, get_directory

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

class TestMain(unittest.TestCase):
    def test_add(self):

        for i, (doc_tp, num, name, shelf_number) in enumerate([
            ('international passport', '311 020203', 'Александр Пушкин', 3),
            ('passport', '020203', 'Вадим Жулидин', 2),
            ('insurance', '311 ', 'Алексей Пригожин', 4)
        ]):
            with self.subTest(i):
                result = add(doc_tp, num, name, shelf_number)
                self.assertIn(doc_tp, result[0][-1]["type"])
                self.assertIn(num, result[0][-1]["number"])
                self.assertIn(name, result[0][-1]["name"])
                self.assertIn(str(shelf_number), result[1])
                self.assertIn(num, result[1][str(shelf_number)])


    def test_get_name(self):
        for i, (doc_number, expected)  in enumerate([
            ("10006", "Аристарх Павлов"),
            ("101", "Документ не найден"),
            ("5455 028765", "Василий Иванов"),
            (111, "Документ не найден")
        ]):
            with self.subTest(i):
                result = get_name(doc_number)
                self.assertEqual(result, expected)


    def test_get_directory(self):
        for i, (doc_number, expected) in enumerate([
            ("11-2","1"),
            ("311 020203","3"),
            ("11","Полки с таким документом не найдено"),
            ("311 020204", "Полки с таким документом не найдено")
        ]):
            with self.subTest(i):
                result = get_directory(doc_number)
                self.assertEqual(result, expected)
        print(directories)