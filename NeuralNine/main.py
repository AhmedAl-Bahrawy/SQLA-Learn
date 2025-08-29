from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import pandas as pd


Base = declarative_base()

# ===================== Association Table =====================
class ClassStudent(Base):
    __tablename__ = "class_student"
    
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"), primary_key=True)


# ===================== Students =====================
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    grade = Column(String)
    
    # العلاقة many-to-many مع Class
    classes = relationship(
        "Class",
        secondary="class_student",
        back_populates="students"
    )


# ===================== Teachers =====================
class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_num = Column(String)
    subject = Column(String)
    
    # علاقة one-to-many مع Class
    classes = relationship("Class", back_populates="teacher")


# ===================== Classes =====================
class Class(Base):
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True)
    start_time = Column(String)
    days = Column(String)
    
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    
    # علاقة مع Teacher
    teacher = relationship("Teacher", back_populates="classes")
    
    # علاقة many-to-many مع Students
    students = relationship(
        "Student",
        secondary="class_student",
        back_populates="classes"
    )

# ===================== Database Setup =====================
engine = create_engine("sqlite:///school.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ===================== Example Usage =====================
# إنشاء مدرس
teacher = Teacher(name="Ahmed Ali", phone_num="01012345678", subject="Math")

# إنشاء كلاس
class1 = Class(start_time="10:00 AM", days="Mon, Wed", teacher=teacher)

# إنشاء طالب
student = Student(name="Omar", grade="9th")

# ربط الطالب بالكلاس
class1.students.append(student)

# إضافة الكائنات للسيشن
session.add_all([teacher, class1, student])
session.commit()

# ===================== Query Examples =====================
# 1. هات الكلاسات بتاعة مدرس~
for c in teacher.classes:
    print("Class:", c.start_time, c.days)

# 2. هات الطلاب اللي في كلاس
for s in class1.students:
    print("Student:", s.name)

# 3. هات الكلاسات اللي الطالب Omar فيها
for c in student.classes:
    print("Student Omar is in class:", c.days)



df = pd.read_sql("SELECT * FROM classes", engine)
print(df)