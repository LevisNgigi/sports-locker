from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Locker(Base):
    __tablename__ = "lockers"
    
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    combination = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))  # Define sport_id column
    

    def __repr__(self):
        return f'Id: {self.id}, Number: {self.number}, Combination: {self.combination}'


class Sport(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    student_id = Column(Integer, ForeignKey("students.id"))

    def __repr__(self):
        return f'Id: {self.id}, Name: {self.name}'


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    grade_level = Column(Integer)

    sports = relationship("Sport", backref=backref('student'))
    lockers = relationship("Locker", backref=backref('student'))


    def __repr__(self):
        return f'Id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}, Grade Level: {self.grade_level}'