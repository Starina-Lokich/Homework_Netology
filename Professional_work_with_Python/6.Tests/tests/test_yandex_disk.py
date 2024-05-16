import unittest
from Task_2_YandexDisk import YandexDisk

TOKEN = 'укажите свой яндекс_токен'


class TestYandexDisk(unittest.TestCase):
    def setUp(self) -> None:
        self.ya_disk = YandexDisk(TOKEN)

    def tearDown(self) -> None:
        del self.ya_disk


    def test_create_and_delete_folder(self):
        '''
        Создание и последующее удаление папки

        (Производится проверка статуса кода при корректной работе функций)
        '''
        self.assertEqual(201, self.ya_disk.create_folder('test'))
        self.assertEqual(204, self.ya_disk.delete_folder('test'))

    def test_foldef_info(self):
        '''
        Получение информации о папке

        (Производится проверка статуса кода при корректной работе функции)
        '''
        self.assertEqual(201, self.ya_disk.create_folder('test'))
        self.assertEqual(200, self.ya_disk.folder_info('test')[1])
        self.assertEqual(204, self.ya_disk.delete_folder('test')) 