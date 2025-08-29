from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, ForeignKey, Time
)

# إنشاء محرك SQLite
engine = create_engine('sqlite:///students.db', echo=True)

# تعريف الـ Metadata
meta = MetaData()

# جدول الطلاب
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False)
)

# جدول المدرسين
teachers = Table(
    'teachers', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False),   # العمر عدد صحيح
    Column('subject', String, nullable=False),
    Column('phone_num', String, nullable=True)  # رقم تليفون نص مش Float
)

# جدول الحصص
classes = Table(
    'classes', meta,
    Column('id', Integer, primary_key=True),
    Column('start_time', Time, nullable=True),
    Column('teacher_id', Integer, ForeignKey('teachers.id'))  # كل كلاس له مدرس واحد
)

# جدول وسيط لعلاقة Many-to-Many بين الطلاب والحصص
class_students = Table(
    'class_students', meta,
    Column('class_id', Integer, ForeignKey('classes.id')),
    Column('student_id', Integer, ForeignKey('students.id'))
)

# إنشاء كل الجداول
meta.create_all(engine)
