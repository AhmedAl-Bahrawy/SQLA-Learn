from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

# ----- Database Config -----
engine = create_engine(
    'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"),
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# ----- Models -----

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)


class Student(BaseModel):
    __tablename__ = "students"
    name = Column(String)
    grade = Column(Integer)
    courses = relationship("Course", secondary="student_course", back_populates="students")


class Course(BaseModel):
    __tablename__ = "courses"
    name = Column(String)
    teacher = relationship("Teacher", back_populates="courses")
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    students = relationship("Student", secondary="student_course")
    
    
class Teacher(BaseModel):
    __tablename__ = "teachers"
    name = Column(String)
    subject = Column(String)
    courses = relationship("Course", back_populates="teacher")


class StudentCourse(BaseModel):
    __tablename__ = "student_course"
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)



Ahmed = Student(name="Ahmed", grade=10)
Ali = Student(name="Ali", grade=10)
Mohammed = Student(name="Mohammed", grade=10)


Mr_Emad = Teacher(name="Mr. Emad", subject="Math")
Mr_Mahmoud = Teacher(name="Mr. Mahmoud", subject="Science")
Mr_Helmy = Teacher(name="Mr. Helmy", subject="English")


Mathatics = Course(name="Math", teacher=Mr_Emad)
Science = Course(name="Science", teacher=Mr_Mahmoud)
English = Course(name="English", teacher=Mr_Helmy)


session.add_all([Ahmed, Ali, Mohammed, Mr_Emad, Mr_Mahmoud, Mr_Helmy, Mathatics, Science, English])
session.commit()

Ahmed.courses.append(Mathatics)
Ali.courses.append(Science)
Mohammed.courses.append(English)

session.commit()





