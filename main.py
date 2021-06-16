class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return "ошибка"

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f"Имя: {self.name}\n=\"" \
              f"Фамилия: {self.surname}\n"\
              f"Сердняя оценка за ДЗ: {self.get_avg_grade()}"
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print("Такого студента нет")
            return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f"{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}")
            else:
                print(f"{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}")
            return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f"Имя: {self.name}\n=\"" \
              f"Фамилия: {self.surname}\n" \
              f"Сердняя оценка за ДЗ: {self.get_avg_grade()}"
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя {self.name}\n"\
              f"Фамилия: {self.surname}\n"
        return res

def get_avg_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list, 2))

def get_avg_lect_grade(list_lect):
    total_sum = 0
    for lecturer in list_lect:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
        return total_sum / len(list_lect)



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
