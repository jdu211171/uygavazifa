from typing import List


class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Course:

    def __init__(self, name: str, teacher: str, students_count=0, students: List[Student] = None):
        self.name = name
        self.teacher = teacher
        self.students_count = students_count
        self.students = students

    def add(self, new_student: Student):
        return self.students.append(new_student)

    def delete(self, student: Student):
        return self.students.remove(student)

    def course_info(self):
        return (f'course name: {self.name}\n'
                f'course teacher: {self.teacher}\n'
                f'attending students count: {self.students_count}\n'
                f'attending students list: {self.students}\n')


islom = Student('Nur Islom', 22)
ferangiz = Student('Ferangiz', 19)
zayniddin = Student('Zayniddin', 20)
ahror = Student('Ahror', 20)
shodiya = Student('Shodiya', 18)
physics_students = [islom, ferangiz, zayniddin, ahror, shodiya]

farangiz = Student('Farangiz', 19)
sevinch = Student('Sevinch', 20)
mushtariy = Student('Mushtariybegim', 20)
aziz = Student('Aziz', 19)
shehroz = Student('Shehrozbek', 20)
math_students = [farangiz, sevinch, mushtariy, aziz, shehroz]

math = Course('Math', 'Asadbek', 5, math_students)
physics = Course('Physics', 'Dilrabo', 5, physics_students)

math.delete(farangiz)
math.delete(mushtariy)

physics.delete(islom)
physics.delete(ferangiz)

print('Physics students')
for student in physics.students:
    print(student.name)
print()
print('Math students')
for student in math.students:
    print(student.name)
