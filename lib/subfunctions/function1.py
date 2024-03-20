from db.models import Locker, Student, Sport
from db.models import Sport
import re
import inquirer
import pandas




def function1a(session, search_option):
    print(" ")
    print("Search for locker combinations by locker number or student last name.")
    while search_option:
        print(" ")
        combo_search = input("Enter locker number or student last name: ")
        print(" ")
        int_pattern = r'\d'
        regex = re.compile(int_pattern)
        match = regex.search(combo_search)
        if combo_search == "Q":
            break
        elif match:
            print_combo_by_locker_number(session, locker_number=combo_search)
        elif not match:
            print_combo_by_last_name(session, last_name=combo_search)

def print_combo_by_locker_number(session, locker_number):
    combo = session.query(Locker).filter(Locker.number == locker_number).first()
    if combo:
        print(f'Locker: {combo.number} Combination: {combo.combination}')
    else:
        print("There is no matching locker number in the database.")

def print_combo_by_last_name(session, last_name):
    students = session.query(Student).filter(Student.last_name == last_name).all()
    if students:
        if len(students) == 1:
            student_lockers = session.query(Locker).join(Student).filter(Student.id == Locker.student_id).filter(Student.last_name == last_name).all()
            if student_lockers:
                print("The selected student has the following locker(s) assigned: ")
                print(" ")
                for locker in student_lockers:
                    print(f'Locker: {locker.number} Combination: {locker.combination}')
            else:
                print(f"Last Name: {last_name} | This student does not have any lockers assigned.")
        else:
            options = []
            print(f"There are multiple students with the last name: {last_name}")
            print(" ")
            for student in students:
                option = (f'{last_name}, {student.first_name}', student.id)
                options.append(option)
            questions = [
                inquirer.List('students',
                              message="Please select the correct student: ",
                              choices=options,
                              ),
                              ]
            answers = inquirer.prompt(questions)
            selection = answers['students']

            student_lockers = session.query(Locker).join(Student).filter(Student.id == Locker.student_id).filter(Locker.student_id == selection).all()
            if student_lockers:
                print("The selected student has the following locker(s) assigned: ")
                print(" ")
                for locker in student_lockers:
                    print(f'Locker: {locker.number} Combination: {locker.combination}')
            else:
                print(f"Last Name: {last_name} | This student does not have any lockers assigned.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function1b(session, search_option):
    print(" ")
    print("Search for sport by student last name.")
    while search_option:
        print(" ")
        record = input("Enter student last name: ")
        print(" ")
        if record == "Q":
            break
        else:
            print_student_sport(session, last_name=record)

def print_student_sport(session, last_name):
    students = session.query(Student).filter(Student.last_name == last_name).all()
    if students:
        if len(students) == 1:
            for student in students:
                sport = session.query(Sport).filter(Sport.student_id == student.id).all()
                if sport:
                    print(f"This student plays the following sport(s) : ")
                    print(" ")
                    sport_data = ([sport.type for sport in sport])
                    df = pandas.DataFrame(sport_data, columns=["Sport"])
                    print(df.to_string(index=False))
                else:
                    print(f"Last Name: {last_name} | There are no sports matching the last name entered.")
        else:
            options = []
            print(f"There are multiple students with the last name: {last_name}")
            print(" ")
            for student in students:
                option = (f'{last_name}, {student.first_name}', student.id)
                options.append(option)
            questions = [
                inquirer.List('students',
                              message="Please select the correct student: ",
                              choices=options,
                              ),
            ]
            answers = inquirer.prompt(questions)
            selection = answers['students']
            student_sport = session.query(Sport).filter(Sport.student_id == selection).all()
            if student_sport:
                print(f"This student plays the following sport(s): ")
                print(" ")
                sport = [sport.type for sport in student_sport]
                df = pandas.DataFrame(sport, columns=["Sport"])
                print(df.to_string(index=False))
            else:
                print(f"Last Name: {last_name} | There are no sports assigned to a student matching the last name entered.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function1c(session, search_option):
    print(" ")
    print("Search for individual students by student last name.")
    while search_option:
        print(" ")
        record = input("Enter student last name: ")
        print(" ")
        if record == "Q":
            break
        else:
            find_by_last_name(session, last_name=record)

def find_by_last_name(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        student_data = ([(student.last_name, student.first_name, student.grade_level) for student in students])
        df = (pandas.DataFrame(student_data, columns=["Last Name", "First Name", "Grade"]))
        print(df.to_string(index=False))
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")