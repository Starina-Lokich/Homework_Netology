import os
import logging
from functools import wraps
from datetime import datetime

# __________ЗАДАНИЕ 1__________
loggers = logging.getLogger(__name__)


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        logging.basicConfig(filename='main.log', filemode='a',level=logging.INFO)
        log_datatime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # дата и время вызова функции
        func_name = old_function.__name__ # имя функции
        result = old_function(*args, **kwargs) # возвращяемое значение
        arg_old_func = [*args] #позиционные аргументы
        f = {**kwargs} # именованные аргументы
        loggers.info(f'{log_datatime} {func_name:<15} | {result:^20} | *args - {str(arg_old_func):<20} | **kwargs - {f}') 
        return result
    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

