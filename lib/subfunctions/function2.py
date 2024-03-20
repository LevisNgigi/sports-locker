from db.models import Student, Sport
import pandas

def function2a(session, search_option):
    print(" ")
    print("Print a list of students by grade level including a final count of students.")
    print(" ")
    print("Press Q to exit to main menu.")
    while search_option:
        print(" ")
        grade = input("Enter grade level: ")
        if grade == "9" or grade == "10" or grade == "11" or grade == "12":
            print_students_by_grade(session, grade=grade)
            print(" ")
            count_students_by_grade(session, grade=grade)
        elif grade == "Q":
            break
        else:
            print(f"You entered: {grade}, which is invalid. Please enter 9, 10, 11, or 12 to print students by grade level.")

def print_students_by_grade(session, grade):
    students = (session.query(Student).filter(Student.grade_level == grade)).all()
    student_data = ([(student.first_name, student.last_name) for student in students])
    df = (pandas.DataFrame(student_data, columns=["First Name", "Last Name"]))
    print(df.to_string(index=False))

def count_students_by_grade(session, grade):
    grade_count = (session.query(Student).filter(Student.grade_level == grade).count())
    print(f"There are {grade_count} student(s) in grade {grade}.")

def function2b(session, search_option):
    print(" ")
    print("Count the number of sports in inventory.")
    print(" ")
    print("Press Q to exit to main menu.")
    while search_option:
        print(" ")
        sport = input("Enter sport type: ")
        sport_types = ["Soccer", "Basketball", "Volleyball", "Tennis", "Swimming", "Baseball", "Softball", "Track and Field", "Cross Country", "Golf"]
        if sport in sport_types:
            print(" ")
            count_sports(session, sport=sport)
        elif sport == "Q":
            break
        else:
            print(f"You entered: {sport}, which is invalid.")
            print("Please select from the following list of sports:")
            print([record for record in sport_types])

def count_sports(session, sport):
    sport_count = session.query(Sport).filter(Sport.type.like(sport)).count()
    if sport_count > 0:
        print(f"There are {sport_count} {sport}(s) in the database.")
    if sport_count == 0:
        print("None of this sport type are currently in the database.")
