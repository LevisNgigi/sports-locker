from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Locker(Base):
    __tablename__ = "lockers"
    
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    combination = Column(String)
    sport_id = Column(Integer, ForeignKey('sports.id'))  # Define sport_id column
    
    sport = relationship("Sport", back_populates="lockers")

    def __repr__(self):
        return f'Id: {self.id}, Number: {self.number}, Combination: {self.combination}'


class Sport(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="sports")

    lockers = relationship("Locker", back_populates="sport")

    def __repr__(self):
        return f'Id: {self.id}, Name: {self.name}'


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    grade_level = Column(Integer)

    sports = relationship("Sport", back_populates="student")

    def __repr__(self):
        return f'Id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}, Grade Level: {self.grade_level}'
