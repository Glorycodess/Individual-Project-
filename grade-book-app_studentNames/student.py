#!/usr/bin/python3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.grades = {}  # key: course name, value: (grade, credits)
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.grades:
            self.GPA = 0.0
        else:
            total_points = sum(grade * credits for grade, credits in self.grades.values())
            total_credits = sum(credits for grade, credits in self.grades.values())
            self.GPA = total_points / total_credits if total_credits != 0 else 0
        return self.GPA

    def register_for_course(self, course, grade):
        if course.name not in self.grades:
            self.courses_registered.append(course)
            self.grades[course.name] = (grade, course.credits)
        self.calculate_GPA()
