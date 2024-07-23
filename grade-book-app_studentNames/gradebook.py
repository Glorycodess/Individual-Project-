import json
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        return course

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            return True
        return False

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        return [(student.names, student.GPA) for student in self.student_list]

    def search_by_grade(self, course_name, min_grade):
        results = []
        for student in self.student_list:
            if course_name in student.grades:
                grade, credits = student.grades[course_name]
                if grade >= min_grade:
                    results.append((student.names, grade))
        return results

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if not student:
            return None
        transcript = {
            "names": student.names,
            "email": student.email,
            "courses": [(course_name, grade) for course_name, (grade, credits) in student.grades.items()],
            "GPA": student.GPA
        }
        return transcript

    def save_data(self, student_file='students.json', course_file='courses.json'):
        with open(student_file, 'w') as sf:
            json.dump([student.__dict__ for student in self.student_list], sf)
        with open(course_file, 'w') as cf:
            json.dump([course.__dict__ for course in self.course_list], cf)

    def load_data(self, student_file='students.json', course_file='courses.json'):
        try:
            with open(student_file, 'r') as sf:
                students = json.load(sf)
                self.student_list = [self.create_student_from_dict(s) for s in students]
            with open(course_file, 'r') as cf:
                courses = json.load(cf)
                self.course_list = [self.create_course_from_dict(c) for c in courses]
        except FileNotFoundError:
            print("Data files not found, starting with empty grade book.")

    @staticmethod
    def create_student_from_dict(data):
        student = Student(data['email'], data['names'])
        student.courses_registered = data['courses_registered']
        student.grades = data['grades']
        student.GPA = data['GPA']
        return student

    @staticmethod
    def create_course_from_dict(data):
        return Course(data['name'], data['trimester'], data['credits'])
