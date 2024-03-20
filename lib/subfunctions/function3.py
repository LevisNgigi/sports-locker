from db.models import Student, Sport

def function3a(session, search_option):
    print(" ")
    print("Add new student to database.")
    while search_option:
        print(" ")
        last_name = input("Enter student last name: ")
        if last_name == "Q":
            break
        else:
            first_name = input("Enter student first name: ")
            grade_level = input("Enter student grade level: ")
            if grade_level == "9" or grade_level == "10" or grade_level == "11" or grade_level == "12":
                print(" ")
                print(f"Last Name: {last_name} | First Name: {first_name} | Grade Level: {grade_level}")
                print(" ")
                confirm = input("Confirm add above student to database? n/Y: ")
                if confirm == "n":
                    print(" ")
                    print("Student NOT added to database.")
                elif confirm == "Y":
                    add_student(session, Student(first_name=first_name, last_name=last_name, grade_level=grade_level))
                    print(" ")
                    print("New student successfully added to database!")
                elif confirm == "Q":
                    break
                else:
                    print (" ")
                    print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")
            else:
                print(" ")
                print(f"You entered Grade Level: {grade_level}, which is an invalid option.")
                print("Please enter 9, 10, 11, or 12 for grade level.")

def add_student(session, student):
    session.add(student)
    session.commit()

def function3b(session, search_option):
    print(" ")
    print("Add new sport to database.")
    while search_option:
        print(" ")
        sport_name = input("Enter sport name: ")
        if sport_name == "Q":
            break
        else:
            print(" ")
            print(f"Sport Name: {sport_name}")
            print(" ")
            confirm = input("Confirm add above sport to database? n/Y: ")
            if confirm == "n":
                print(" ")
                print("Sport NOT added to database.")
            elif confirm == "Y":
                add_sport(session, Sport(name=sport_name))
                print(" ")
                print("New sport successfully added to database!")
            elif confirm == "Q":
                break
            else:
                print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")

def add_sport(session, sport):
    session.add(sport)
    session.commit()
