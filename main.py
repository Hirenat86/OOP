class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name) 

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'  
            
    def ever_grade_st(self):
        total_grade = 0
        sum_grade = 0
        for course in self.grades:
            total_grade += len(self.grades[course])
            sum_grade += sum(self.grades[course])
        if total_grade > 0:
            return sum_grade / total_grade
        else:
            return 0
        
    def __lt__(self, different_st): 
        if not isinstance(different_st, Student): 
            print('Невозможно сравнить разные классы!') 
            return 
        return self.ever_grade_st() < different_st.ever_grade_st()
    
    def __gt__(self, different_st): 
        if not isinstance(different_st, Student): 
            print('Невозможно сравнить разные классы!') 
            return 
        return self.ever_grade_st() > different_st.ever_grade_st()
    
    def __eq__(self, different_st): 
        if not isinstance(different_st, Student): 
            print('Невозможно сравнить разные классы!') 
            return 
        return self.ever_grade_st() == different_st.ever_grade_st()
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self.ever_grade_st()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
 
     
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def add_courses_attached(self, course_attachet):
        self.courses_attached.append(course_attachet)
        
 

class Lecturer(Mentor):
    
    def __init__(self, name, surname, course_attached):
        super().__init__(name, surname)
        super().add_courses_attached(course_attached)
        self.grades = {}
        
    def ever_grade(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0
    
    def __lt__(self, different_st): 
        if not isinstance(different_st, Lecturer): 
            print('Невозможно сравнить разные классы!') 
            return 
        return self.ever_grade() < different_st.ever_grade()
    
    def __gt__(self, different_st): 
        if not isinstance(different_st, Lecturer): 
            print('Невозможно сравнить разные классы!') 
            return 
        return self.ever_grade() > different_st.ever_grade()
    
    def __eq__(self, different_st): 
        if not isinstance(different_st, Lecturer): 
            print('Невозможно сравнить разные классы!') 
            return 
        return self.ever_grade() == different_st.ever_grade()
        
    def __str__(self):
        return (f'Имя: {self.name} \n'
        f'Фамилия: {self.surname} \n'
        f'Средняя оценка за домашние задания: {self.ever_grade()}\n')

class Reviewer(Mentor):
    
    def __init__(self, name, surname, course_attached):
        super().__init__(name, surname)
        super().add_courses_attached(course_attached)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}\n')


student_1 = Student('Семен', 'Иванов', 'male')
student_1.courses_in_progress += ['Python', 'C++']
student_1.finished_courses += ['Office']

student_2 = Student('Анна', 'Смирнова', 'female')
student_2.courses_in_progress += ['Python', 'Exel']
student_2.finished_courses += ['PyCharm']

lecturer_1 = Lecturer('Иван', 'Федулов', 'Python')
lecturer_2 = Lecturer('Роман', 'Никитин', 'Python')

reviewer_1 = Reviewer('Дмитрий', 'Валов', 'Python')
reviewer_1.courses_attached += ['C++', 'PyCharm']

reviewer_2 = Reviewer('София', 'Набокова', 'Python')
reviewer_2.courses_attached += ['JavaScript', 'basic']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Python', 7)
student_1.rate_lecturer(lecturer_2, 'Python', 8)

student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 3)
student_2.rate_lecturer(lecturer_1, 'Python', 7)

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def best_student(student_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in student_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{round(overall_student_rating / lectors, 1)}'


def best_lecturer(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            lecturer_average_rates = 0
            for rate in lecturer.grades[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.grades[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{round(average_rating / b, 1)}'

print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)

if student_1 < student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} меньше, чем средняя оценка {student_2.name} {student_2.surname}\n')
elif student_1 > student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} больше, чем средняя оценка {student_2.name} {student_2.surname}\n')
else:
    print(f'Средняя оценка {student_1.name} {student_1.surname}  равна средней оценке {student_2.name} {student_2.surname}\n')

if lecturer_1 > lecturer_2:
    print(f'Средняя оценка {lecturer_1.name} {lecturer_1.surname} больше, чем средняя оценка {lecturer_2.name} {lecturer_2.surname}\n')
elif lecturer_1 < lecturer_2:
    print(f'Средняя оценка {lecturer_1.name} {lecturer_1.surname} меньше, чем средняя оценка {lecturer_2.name} {lecturer_2.surname}\n')
else:
    print(f'Средняя оценка {lecturer_1.name} {lecturer_1.surname}  равна средней оценке {lecturer_2.name} {lecturer_2.surname}\n')

print(f'Средняя оценка студентов по курсу "Python": {best_student(student_list, "Python")}\n')
print(f'Средняя оценка лекторов по курсу "Python": {best_lecturer(lecturer_list, "Python")}\n')