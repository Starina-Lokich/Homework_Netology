class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка данных'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {self.avarage_grades()}
Курсы в роцессе изучения: {', '.join(self.courses_in_progress) if len(self.courses_in_progress) != 0 else "Отсутствуют"}
Завершенные курсы: {', '.join(self.finished_courses) if len(self.finished_courses) != 0 else "Отсутствуют"}"""

    def avarage_grades(self):
        if len(self.grades) != 0:
            sum_grades = 0
            cout_grades = 0
            for list_grades in self.grades.values():
                for grade in list_grades:
                    sum_grades += grade
                    cout_grades += 1
            return sum_grades / cout_grades
        else:
            return 0

    def __gt__(self, other):
        return self.avarage_grades() > other.avarage_grades()
    
    def __eq__(self, other):
        return self.avarage_grades() == other.avarage_grades()

    def __ne__(self, other):
        return self.avarage_grades() != other.avarage_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avarage_grades(self):
        if len(self.grades) != 0:
            sum_grades = 0
            cout_grades = 0
            for list_grades in self.grades.values():
                for grade in list_grades:
                    sum_grades += grade
                    cout_grades += 1
            return sum_grades / cout_grades
        else:
            return 0

    def __str__(self):
        return f'{super().__str__()}\nСредняя оценка за лекции: {self.avarage_grades()}'

    def __gt__(self, other):
        return self.avarage_grades() > other.avarage_grades()
    
    def __eq__(self, other):
        return self.avarage_grades() == other.avarage_grades()

    def __ne__(self, other):
        return self.avarage_grades() != other.avarage_grades()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка данных'


kirill = Student('Кирилл', 'Попов', 'муж')
kirill.finished_courses += ['Основы языка програмирования Python']
kirill.courses_in_progress += ['Git — система контроля версий']
kirill.grades['Git — система контроля версий'] = [10, 9, 7, 10]


oleg = Student('Олег', 'Фестралов', 'муж')
oleg.finished_courses += ['Основы языка програмирования Python']
oleg.courses_in_progress += ['ООП и работа с API']
oleg.grades['ООП и работа с API'] = [9, 8, 10, 7]

vladimir = Lecturer('Владимир', 'Афонин')
vladimir.courses_attached += ['Git — система контроля версий']
vladimir.grades['Git — система контроля версий'] = [10, 9, 9, 8]
kirill.rate_lecturer(vladimir, 'Git — система контроля версий', 6)

aleksander = Lecturer('Александр', 'Шкода')
aleksander.courses_attached += ['ООП и работа с API']
aleksander.grades['ООП и работа с API'] = [9, 10, 9, 10]
oleg.rate_lecturer(aleksander, 'ООП и работа с API', 9)

vasiliy = Reviewer('Василий', 'Жулидин')
vasiliy.courses_attached += ['ООП и работа с API']
vasiliy.rate_hw(oleg, 'ООП и работа с API', 4)

vaycheslav = Reviewer('Вячеслав', 'Иовенко')
vaycheslav.courses_attached += ['Git — система контроля версий']
vaycheslav.rate_hw(kirill, 'Git — система контроля версий', 5)

print('__Студенты__', '\n', sep='')
print(kirill, '\n', sep='')
print(oleg, '\n', sep='')
print(f'{oleg > kirill} {oleg == kirill} {oleg != kirill}', '\n', sep='')
print('-' * 30, '\n', sep='')

print('__Лекторы__', '\n', sep='')
print(vladimir, '\n', sep='')
print(aleksander, '\n', sep='')
print(f'{aleksander > vladimir} {aleksander == vladimir} {aleksander != vladimir}', '\n', sep='')
print('-' * 30, '\n', sep='')

print('__Проверяющие__', '\n', sep='')
print(vaycheslav, '\n', sep='')
print(vasiliy, '\n', sep='')
print('-' * 30, '\n', sep='')

studetn_lust = []
studetn_lust += [kirill, oleg]

lecturer_list = []
lecturer_list += [vladimir, aleksander]

def average_score_all(input_list):
    average_score = 0
    for student in input_list:
        average_score += student.avarage_grades()
    return average_score

print(f'''Средний бал у лекторов: {average_score_all(lecturer_list):.1f}
Средний бал у студентов: {average_score_all(studetn_lust):.1f}''')
