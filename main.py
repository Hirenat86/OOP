class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'  
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
 
     
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
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
 

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
        return f'Имя: {self.name} \nФамилия: {self.surname}'

student = Student("dmitriy","Petukhov","M")
print(student)


# rev = Reviewer('ivan', 'Ivanov', 'py')
# print (rev.courses_attached)
# rev.add_courses_attached('dfd')
# print (rev.courses_attached)

# def str(self):
# return f’Имя: {self.name}\n’
# f’Фамилия: {self.surname}\n’
# f’Средняя оценка за домашние задания: {self.ever_grade()}\n’
# f’Курсы в процессе изучения: {", “.join(self.courses_in_progress)}\n’
# f’Завершенные курсы: {”, ".join(self.finished_courses)}’

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)