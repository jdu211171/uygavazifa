class Time:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second


class Timetable:
    def __init__(self, subject: str, time: Time, classroom: int):
        self.subject = subject
        self.time = time
        self.classroom = classroom


math = Timetable("Math", Time(9, 0, 0), 101)
physics = Timetable("Physics", Time(10, 0, 0), 102)
chemistry = Timetable("Chemistry", Time(11, 0, 0), 103)
biology = Timetable("Biology", Time(12, 0, 0), 104)
english = Timetable("English", Time(13, 0, 0), 105)
history = Timetable("History", Time(14, 0, 0), 106)
geography = Timetable("Geography", Time(15, 0, 0), 107)
computer = Timetable("Computer", Time(16, 0, 0), 108)
music = Timetable("Music", Time(17, 0, 0), 109)
art = Timetable("Art", Time(18, 0, 0), 110)
courses = [math, physics, chemistry, biology, english, history, geography, computer, music, art]
user = Time(int(input('Enter hour: ')), int(input('Enter minute: ')), int(input('Enter second: ')))
for course in courses:
    if course.time.hour == user.hour and course.time.minute == user.minute and course.time.second == user.second:
        print(f"Subject: {course.subject}, Time: {course.time.hour}:{course.time.minute}:{course.time.second}, Classroom: {course.classroom}")
