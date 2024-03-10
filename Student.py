class Student:
    name = ''
    group = ''
    grades = []
    age = 0
    gpa = 0

    def __init__(self, name, group = '', age = 0, grades = ()):
        self.name = name
        self.group = group
        self.age = age
        self.grades = grades
        if grades:
            self.gpa = round(sum(self.grades) / len(grades), 2)
    def show_info(self):
        print(f'{self.name} ({self.age} age), group {self.group}')
        print(f'Середній блал: ({self.gpa}  ({self.grades})')


student1 = Student(name='Katya' , group='B2121' , age=12, grades=[8, 7, 9, 10, 8, 8, 6])

student2 = Student(name = 'Roma')

student2.age = 12
student2.group = 'B2121'
student2.grades = [6, 6, 5, 7, 6, 6, 8]

student1.show_info()
student2.show_info()