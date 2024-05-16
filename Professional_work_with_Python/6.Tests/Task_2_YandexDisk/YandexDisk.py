import requests


class YandexDisk:

    def __init__(self, yandex_token: str):
        self.yandex_token = yandex_token
        self.url = "https://cloud-api.yandex.net/v1/disk/"
        self.headers = {
            'Content-Type': 'application/json',
            "Authorization": yandex_token
        }

    def create_folder(self, name_folder: str) -> int:
        '''
        Функция создает папку на YandexDisk

        Возвращает статус кода
        '''

        self.params = {
            "path" : name_folder
        }
        response = requests.put(self.url + "resources", 
                                    headers=self.headers, 
                                    params=self.params)
        return response.status_code

    def folder_info(self, name_folder: str) -> tuple[dict,int]:
        '''
        Возвращает кортеж, в котором словарь с данными о папке и статус кода
        '''
        self.params = {
            "path" : name_folder
        }
        result = requests.get(self.url + "resources", 
                              headers=self.headers,
                              params=self.params)
        return result.json(), result.status_code
    
    def delete_folder(self, name_folder: str) -> int:
        '''
        Функция создает папку на YandexDisk

        Возвращает статус кода
        '''

        self.params = {
            "path" : name_folder
        }
        response = requests.delete(self.url + "resources", 
                                    headers=self.headers, 
                                    params=self.params)
        return response.status_code