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
Средняя оценка за домашнее задание: {self._avarage_grades()}
Курсы в роцессе изучения: {', '.join(self.courses_in_progress) if len(self.courses_in_progress) != 0 else "Отсутствуют"}
Завершенные курсы: {', '.join(self.finished_courses) if len(self.finished_courses) != 0 else "Отсутствуют"}"""

    def _avarage_grades(self):
        if len(self.grades) != 0:
            sum_grades = 0
            cout_grades = 0
            for list_grades in self.grades.value():
                for grade in list_grades:
                    sum_grades += grade
                    cout_grades += 1
            return sum_grades / cout_grades
        else:
            return 0

    def __gt__(self, other):
        return self._avarage_grades() > other._avarage_grades()

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

    def _avarage_grades(self):
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
        return f'{super().__str__()}\nСредняя оценка за лекции: {self._avarage_grades()}'

    def __gt__(self, other):
        return self._avarage_grades() > other._avarage_grades()

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
