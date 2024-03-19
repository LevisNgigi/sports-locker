from faker import Faker
from random import choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Locker, Sport, Student  # Import Base from models

fake = Faker()

engine = create_engine("sqlite:///sports_lockers.db")
session = Session(engine, future=True)

def delete_records():
    Base.metadata.create_all(engine)  # Ensure all tables are created
    session.query(Locker).delete()
    session.query(Sport).delete()
    session.query(Student).delete()
    session.commit()

def create_records():
    # students
    grade_levels = [9, 10, 11, 12]
    students = [Student(
        first_name=f'{fake.first_name()}',
        last_name=f'{fake.last_name()}',
        grade_level=rc(grade_levels)
    ) for i in range(80)]

    # lockers
    lockers = [Locker(
        number = fake.unique.random_int(min=1, max=150),
        combination = f'{fake.random_int(min=0, max=39)}-{fake.random_int(min=0, max=39)}-{fake.random_int(min=0, max=39)}',
        sport_id = fake.random_int(min=1, max=80)
    ) for i in range(150)]

    # sports
    sport_names = ["Football", "Basketball", "Soccer", "Baseball", "Tennis", "Volleyball", "Swimming", "Track and Field", "Golf"]
    sports = [Sport(
        name = rc(sport_names),
        student_id = fake.random_int(min=1, max=80)
    ) for i in range(80)]

    session.add_all(students + lockers + sports)
    session.commit()
    return students, lockers, sports

def relate_records(students, lockers, sports):
    for student in students:
        student.locker = rc(lockers)
        student.sport = rc(sports)
    
    session.add_all(students)
    session.commit()

if __name__ == "__main__":
    delete_records()
    create_records()

    session.close()
    session.commit()
