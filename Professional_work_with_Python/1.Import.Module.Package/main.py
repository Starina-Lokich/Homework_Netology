import application.salary as salary
import application.db.people as peaple
from datetime import datetime

from tqdm import tqdm
from time import sleep


if __name__ == '__main__':
    t =datetime.today()
    print(t.strftime("%d-%b-%Y %H:%M:%S"))
    salary.calculate_salary()
    peaple.get_employees()

    from tqdm import tqdm
    from time import sleep

    # функция с задержкой исполнения
    def fun(x):
        sleep(x/4)
        return x

        # цикл с прогресс-баром
    for i in tqdm(range(10)):
        fun(i)
    print('Данные загружены')
    