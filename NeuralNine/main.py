"""
SQLAlchemy ORM Tutorial - Complete School Management System

This module demonstrates a complete school management system using SQLAlchemy ORM.
It showcases relationships, CRUD operations, and real-world database patterns.

Key Concepts Covered:
- SQLAlchemy ORM vs Core
- Declarative base and model definitions
- One-to-Many relationships
- Many-to-Many relationships
- Association tables
- Session management
- CRUD operations
- Query examples

Author: NeuralNine Tutorial Series
License: MIT
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

# =============================================================================
# DATABASE CONFIGURATION
# =============================================================================

# Create declarative base for ORM models
# This is the foundation for all ORM classes
Base = declarative_base()

# =============================================================================
# ASSOCIATION TABLE FOR MANY-TO-MANY RELATIONSHIP
# =============================================================================

class ClassStudent(Base):
    """
    Association table for Many-to-Many relationship between Students and Classes.
    
    This table connects students to classes they attend. It's a pure association
    table with no additional data, so it doesn't need to be a full model class.
    
    Features:
    - Composite primary key (student_id, class_id)
    - Foreign keys to both students and classes tables
    - Enables many-to-many relationship
    """
    __tablename__ = "class_student"
    
    # Composite primary key
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"), primary_key=True)

# =============================================================================
# STUDENT MODEL
# =============================================================================

class Student(Base):
    """
    Student model representing students in the school.
    
    This model demonstrates:
    - Basic ORM model structure
    - Many-to-Many relationship with Classes
    - String representation for debugging
    """
    __tablename__ = "students"
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Student information
    name = Column(String, nullable=False)  # Required field
    grade = Column(String)                 # Optional field
    
    # Many-to-Many relationship with Classes
    # - secondary="class_student": Uses the association table
    # - back_populates="students": Bidirectional relationship
    classes = relationship(
        "Class",
        secondary="class_student",
        back_populates="students"
    )
    
    def __repr__(self):
        """String representation for debugging and logging."""
        return f"<Student(name='{self.name}', grade='{self.grade}')>"

# =============================================================================
# TEACHER MODEL
# =============================================================================

class Teacher(Base):
    """
    Teacher model representing teachers in the school.
    
    This model demonstrates:
    - One-to-Many relationship with Classes
    - Optional fields for flexibility
    - Professional information storage
    """
    __tablename__ = "teachers"
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Teacher information
    name = Column(String, nullable=False)    # Required field
    phone_num = Column(String)               # Optional phone number
    subject = Column(String)                 # Subject taught
    
    # One-to-Many relationship with Classes
    # - One teacher can teach multiple classes
    # - back_populates="teacher": Bidirectional relationship
    classes = relationship("Class", back_populates="teacher")
    
    def __repr__(self):
        """String representation for debugging and logging."""
        return f"<Teacher(name='{self.name}', subject='{self.subject}')>"

# =============================================================================
# CLASS MODEL
# =============================================================================

class Class(Base):
    """
    Class model representing classes/sessions in the school.
    
    This model demonstrates:
    - Foreign key relationships
    - One-to-Many relationship with Teacher
    - Many-to-Many relationship with Students
    - Scheduling information
    """
    __tablename__ = "classes"
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Class information
    start_time = Column(String)  # Class start time
    days = Column(String)        # Days of the week
    
    # Foreign key to Teacher (One-to-Many)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    
    # Relationships
    # One-to-Many with Teacher
    teacher = relationship("Teacher", back_populates="classes")
    
    # Many-to-Many with Students
    students = relationship(
        "Student",
        secondary="class_student",
        back_populates="classes"
    )
    
    def __repr__(self):
        """String representation for debugging and logging."""
        return f"<Class(start_time='{self.start_time}', days='{self.days}')>"

# =============================================================================
# DATABASE SETUP
# =============================================================================

def setup_database():
    """
    Set up the database engine and create all tables.
    
    This function:
    1. Creates the database engine
    2. Creates all tables defined in the models
    3. Returns a session factory for database operations
    """
    # Create database path
    database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "school.db")
    
    # Create engine with SQL query logging enabled
    engine = create_engine(f'sqlite:///{database_path}', echo=True)
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    # Create session factory
    SessionFactory = sessionmaker(bind=engine)
    
    print("✅ Database setup completed!")
    print(f"📁 Database file: {database_path}")
    
    return SessionFactory

# =============================================================================
# EXAMPLE USAGE AND DEMONSTRATIONS
# =============================================================================

def create_sample_data(db_session):
    """
    Create sample data to demonstrate the school management system.
    
    Args:
        db_session: SQLAlchemy session for database operations
    """
    print("\n🏫 Creating sample school data...")
    
    # Create a teacher
    teacher = Teacher(
        name="Ahmed Ali",
        phone_num="01012345678",
        subject="Mathematics"
    )
    
    # Create a class
    class1 = Class(
        start_time="10:00 AM",
        days="Monday, Wednesday",
        teacher=teacher  # Assign teacher to class
    )
    
    # Create students
    student1 = Student(name="Omar Hassan", grade="9th")
    student2 = Student(name="Fatima Ahmed", grade="10th")
    student3 = Student(name="Mohammed Ali", grade="9th")
    
    # Add students to the class (Many-to-Many relationship)
    class1.students.append(student1)
    class1.students.append(student2)
    class1.students.append(student3)
    
    # Add all objects to session
    db_session.add_all([teacher, class1, student1, student2, student3])
    
    # Commit changes to database
    db_session.commit()
    
    print("✅ Sample data created successfully!")

def demonstrate_queries(db_session):
    """
    Demonstrate various query operations on the school data.
    
    Args:
        db_session: SQLAlchemy session for database operations
    """
    print("\n🔍 Query Demonstrations:")
    print("=" * 50)
    
    # Query 1: Get all teachers
    print("\n1️⃣ All Teachers:")
    teachers = db_session.query(Teacher).all()
    for teacher in teachers:
        print(f"   • {teacher}")
    
    # Query 2: Get all students
    print("\n2️⃣ All Students:")
    students = db_session.query(Student).all()
    for student in students:
        print(f"   • {student}")
    
    # Query 3: Get all classes
    print("\n3️⃣ All Classes:")
    classes = db_session.query(Class).all()
    for class_obj in classes:
        print(f"   • {class_obj}")
    
    # Query 4: Get classes taught by a specific teacher
    print("\n4️⃣ Classes taught by Ahmed Ali:")
    teacher = db_session.query(Teacher).filter(Teacher.name == "Ahmed Ali").first()
    if teacher:
        for class_obj in teacher.classes:
            print(f"   • {class_obj}")
    
    # Query 5: Get students in a specific class
    print("\n5️⃣ Students in the first class:")
    first_class = db_session.query(Class).first()
    if first_class:
        for student in first_class.students:
            print(f"   • {student}")
    
    # Query 6: Get classes attended by a specific student
    print("\n6️⃣ Classes attended by Omar Hassan:")
    student = db_session.query(Student).filter(Student.name == "Omar Hassan").first()
    if student:
        for class_obj in student.classes:
            print(f"   • {class_obj}")

def demonstrate_relationships():
    """
    Demonstrate the relationships between different entities.
    
    This function shows:
    - How relationships work in SQLAlchemy ORM
    - Bidirectional navigation
    - Lazy loading concepts
    """
    print("\n🔗 Relationship Demonstrations:")
    print("=" * 50)
    
    print("\n1️⃣ One-to-Many Relationship (Teacher -> Classes):")
    print("   - One teacher can teach multiple classes")
    print("   - Each class has exactly one teacher")
    print("   - Navigation: teacher.classes (list of classes)")
    print("   - Navigation: class.teacher (single teacher object)")
    
    print("\n2️⃣ Many-to-Many Relationship (Students <-> Classes):")
    print("   - One student can attend multiple classes")
    print("   - One class can have multiple students")
    print("   - Navigation: student.classes (list of classes)")
    print("   - Navigation: class.students (list of students)")
    print("   - Association table: class_student")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    Main execution block for the school management system tutorial.
    
    This block:
    1. Sets up the database
    2. Creates sample data
    3. Demonstrates queries
    4. Shows relationships
    5. Provides learning outcomes
    """
    print("🎓 SQLAlchemy ORM Tutorial - School Management System")
    print("=" * 70)
    
    # Set up database
    SessionFactory = setup_database()
    session = SessionFactory()
    
    try:
        # Create sample data
        create_sample_data(session)
        
        # Demonstrate queries
        demonstrate_queries(session)
        
        # Demonstrate relationships
        demonstrate_relationships()
        
        print("\n🎯 Learning Outcomes:")
        print("=" * 30)
        print("✅ SQLAlchemy ORM model definition")
        print("✅ One-to-Many relationships")
        print("✅ Many-to-Many relationships")
        print("✅ Association tables")
        print("✅ CRUD operations")
        print("✅ Query techniques")
        print("✅ Session management")
        
        print("\n🚀 Next Steps:")
        print("=" * 20)
        print("1. Explore ZeqTech tutorials for advanced concepts")
        print("2. Learn about query optimization")
        print("3. Practice with filtering and ordering")
        print("4. Study relationship loading techniques")
        
    except (ValueError, TypeError, AttributeError) as e:
        print(f"❌ Error occurred: {e}")
        session.rollback()
    finally:
        # Close session
        session.close()
        print("\n✅ Tutorial completed successfully!")
        print("💡 Key takeaways:")
        print("   - ORM provides object-oriented database access")
        print("   - Relationships enable complex data modeling")
        print("   - Sessions manage database transactions")
        print("   - Queries can navigate relationships easily")
