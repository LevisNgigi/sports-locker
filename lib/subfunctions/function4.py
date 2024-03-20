from db.models import Locker, Student, Sport
import inquirer
import re

def function4a(session, search_option):
    print(" ")
    print("Assign or reassign locker to student.")
    while search_option:
        print(" ")
        last_name = input("Enter student last name: ")
        if last_name == "Q":
            break
        else:
            assign_locker(session, last_name)

def assign_locker(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        options = []
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
        locker = input("Enter locker number to assign to student: ")
        int_pattern = r'\d'
        regex = re.compile(int_pattern)
        match = regex.search(locker)
        if match:
            exists = session.query(Locker).filter(Locker.number == locker).first()
            if exists.student_id:
                print(" ")
                reassign = input(f"Locker: {locker} is currently assigned to student ID: {exists.student_id}. Reassign? n/Y: ")
                if reassign == "Y":
                    print(" ")
                    print(f"Last Name: {last_name} | Locker: {locker}")
                    print(" ")
                    confirm = input(f"Confirm above locker assignment? n/Y: ")
                    if confirm == "Y":
                        session.query(Locker).filter(Locker.number == locker).update({
                            Locker.student_id: selection
                            })
                        session.commit()
                        print(" ")
                        print("Locker assignment successfully updated!")
                    elif confirm == "n":
                        print(" ")
                        print("Locker assignment NOT updated.")
                    else:
                        print(" ")
                        print("Invalid entry. Please enter n/Y.")
                else:
                    print(" ")
                    print("Locker assignment NOT updated.")
            else:
                print(" ")
                print(f"Locker {locker} does not exist in the database.")
                print("Please add this locker before assigning it, or choose an existing locker number to assign.")
        else:
            print(" ")
            print("Invalid entry. Locker number must be an integer.")
    else:
        print(" ")
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function4b(session, search_option):
    print(" ")
    print("Assign or reassign sport to student.")
    while search_option:
        print(" ")
        last_name = input("Enter student last name: ")
        if last_name == "Q":
            break
        else:
            assign_sport(session, last_name)

def assign_sport(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        options = []
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
        sport_id = input("Enter sport ID to assign to student: ")
        int_pattern = r'\d'
        regex = re.compile(int_pattern)
        match = regex.search(sport_id)
        if match:
            sport = session.query(Sport).filter(Sport.id == sport_id).first()
            if sport.student_id:
                print(" ")
                reassign = input(f"Sport ID: {sport_id} is currently assigned to student ID: {sport.student_id}. Reassign? n/Y: ")
                if reassign == "Y":
                    print(" ")
                    print(f"Sport ID: {sport_id} | Name: {sport.name} | Last Name: {last_name}")
                    print(" ")
                    confirm = input(f"Confirm above sport assignment? n/Y: ")
                    if confirm == "Y":
                        session.query(Sport).filter(Sport.id == sport_id).update({
                            Sport.student_id: selection
                            })
                        session.commit()
                        print(" ")
                        print("Sport assignment successfully updated!")
                    elif confirm == "n":
                        print(" ")
                        print("Sport assignment NOT updated.")
                    else:
                        print(" ")
                        print("Invalid entry. Please enter n/Y.")
                else:
                    print(" ")
                    print("Sport assignment NOT updated.")
            else:
                print(" ")
                print(f"Sport with ID: {sport_id} does not exist in the database.") 
                print("Please add this sport before assigning it, or choose an existing sport ID to assign.")
        else:
            print(" ")
            print("Invalid entry. Sport ID must be an integer.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function4c(session, search_option):
    print(" ")
    print("Update student information.")
    while search_option:
        print(" ")
        last_name = input("Enter student last name: ")
        if last_name == "Q":
            break
        else:
            update_student_info(session, last_name)

def update_student_info(session, last_name):
    students = (session.query(Student).filter(Student.last_name == last_name).all())
    if students:
        options = []
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
        last_name = input("Enter updated student last name: ")
        first_name = input("Enter updated student first name: ")
        grade_level = input("Enter updated student grade level: ")
        if grade_level == "9" or grade_level == "10" or grade_level == "11" or grade_level == "12":
            print(" ")
            print(f"Last Name: {last_name} | First Name: {first_name} | Grade Level: {grade_level}")
            print(" ")
            confirm = input(f"Confirm update above student record? n/Y: ")
            if confirm == "Y":
                session.query(Student).filter(Student.id == selection).update({
                    Student.first_name: first_name,
                    Student.last_name: last_name,
                    Student.grade_level: grade_level
                    })
                session.commit()
                print(" ")
                print("Student record successfully updated!")
            elif confirm == "n":
                print(" ")
                print("Student record NOT updated.")
            else:
                print(" ")
                print("Invalid entry. Please enter n/Y.")
        else:
            print(" ")
            print(f"You entered: {grade_level}, which is not a valid grade level.")
            print("Please enter grade level 9, 10, 11, or 12.")
    else:
        print(f"Last Name: {last_name} | There is no student matching this name in the database.")

def function4d(session, search_option):
    print(" ")
    print("Increase all student grade levels by one year.")
    while search_option:
        print(" ")
        confirm = input("Confirm update ALL student grade levels to increase by one year? n/Y: ")
        if confirm == "Y":
            print(" ")
            confirm_confirm = input("WARNING: Selecting Y will update ALL student grade levels to increase by one year. Press n/Y to confirm: ")
            if confirm_confirm == "Y":
                increase_grade_levels(session)
                print(" ")
                print("Successfully increased all student grade levels by one year.")
                break
            else: 
                print("Student records NOT updated.")
                break
        else:
            print("Student records NOT updated.")
            break

def increase_grade_levels(session):
    session.query(Student).update({
        Student.grade_level: Student.grade_level + 1
        })
    session.commit()
