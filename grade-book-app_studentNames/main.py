#!/usr/bin/python3

from gradebook import GradeBook

def user_interface():
    gradebook = GradeBook()
    gradebook.load_data()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Save and Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("Student added successfully.")

        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print("Course added successfully.")

        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            if gradebook.register_student_for_course(student_email, course_name, grade):
                print("Student registered for course successfully.")
            else:
                print("Failed to register student for course.")

        elif choice == "4":
            ranking = gradebook.calculate_ranking()
            print("Student Ranking (Name, GPA):")
            for rank, (names, gpa) in enumerate(ranking, start=1):
                print(f"{rank}. {names} - GPA: {gpa:.2f}")

        elif choice == "5":
            course_name = input("Enter course name: ")
            min_grade = float(input("Enter minimum grade: "))
            results = gradebook.search_by_grade(course_name, min_grade)
            print(f"Students who scored at least {min_grade} in {course_name}:")
            for names, grade in results:
                print(f"{names} - Grade: {grade:.2f}")

        elif choice == "6":
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"Transcript for {transcript['names']}:")
                for course, grade in transcript["courses"]:
                    print(f"{course}: {grade}")
                print(f"GPA: {transcript['GPA']:.2f}")
            else:
                print("Student not found.")

        elif choice == "7":
            gradebook.save_data()
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interface()
