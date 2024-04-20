import application.salary as salary
import application.db.people as peaple
from datetime import datetime



if __name__ == '__main__':
    t =datetime.today()
    print(t.strftime("%d-%b-%Y %H:%M:%S"))
    salary.calculate_salary()
    peaple.get_employees()
