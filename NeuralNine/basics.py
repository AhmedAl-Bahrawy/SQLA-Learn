"""
SQLAlchemy Basics Tutorial - Core Concepts and Table Creation

This module demonstrates the fundamental concepts of SQLAlchemy using the Core approach.
It covers table creation, relationships, and basic database operations without the ORM layer.

Key Concepts Covered:
- SQLAlchemy Core vs ORM
- Database engine creation
- Metadata and table definitions
- Column types and constraints
- Foreign key relationships
- Many-to-Many relationships
- Database schema creation

Author: NeuralNine Tutorial Series
License: MIT
"""

from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, ForeignKey, Time
)
import os

# =============================================================================
# DATABASE CONFIGURATION
# =============================================================================

# Create SQLite database engine
# - echo=True: Enables SQL query logging for debugging
# - Database file: students.db in the same directory as this script
database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.db")
engine = create_engine(f'sqlite:///{database_path}', echo=True)

# Create Metadata object to hold table definitions
# Metadata is a container that holds all table definitions
meta = MetaData()

# =============================================================================
# TABLE DEFINITIONS
# =============================================================================

# Students table - stores student information
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),      # Primary key, auto-increment
    Column('name', String, nullable=False),       # Student name, required
    Column('age', Integer, nullable=False)        # Student age, required
)

# Teachers table - stores teacher information
teachers = Table(
    'teachers', meta,
    Column('id', Integer, primary_key=True),      # Primary key, auto-increment
    Column('name', String, nullable=False),       # Teacher name, required
    Column('age', Integer, nullable=False),       # Teacher age, required
    Column('subject', String, nullable=False),    # Subject taught, required
    Column('phone_num', String, nullable=True)    # Phone number, optional
)

# Classes table - stores class information
classes = Table(
    'classes', meta,
    Column('id', Integer, primary_key=True),      # Primary key, auto-increment
    Column('start_time', Time, nullable=True),    # Class start time, optional
    Column('teacher_id', Integer, ForeignKey('teachers.id'))  # Foreign key to teachers
)

# Association table for Many-to-Many relationship between students and classes
# This table connects students to classes they attend
class_students = Table(
    'class_students', meta,
    Column('class_id', Integer, ForeignKey('classes.id')),    # Foreign key to classes
    Column('student_id', Integer, ForeignKey('students.id'))  # Foreign key to students
)

# =============================================================================
# DATABASE SCHEMA CREATION
# =============================================================================

def create_database_schema():
    """
    Create all tables in the database.
    
    This function:
    1. Creates all tables defined in the metadata
    2. Establishes foreign key relationships
    3. Sets up the complete database schema
    
    Note: In production, use Alembic for database migrations instead of create_all()
    """
    print("🚀 Creating database schema...")
    
    # Create all tables defined in the metadata
    meta.create_all(engine)
    
    print("✅ Database schema created successfully!")
    print(f"📁 Database file: {database_path}")

def display_table_info():
    """
    Display information about the created tables.
    
    This function shows:
    - Table names
    - Column information
    - Foreign key relationships
    """
    print("\n📋 Database Schema Information:")
    print("=" * 50)
    
    # Display information for each table
    for table_name, table in meta.tables.items():
        print(f"\n📊 Table: {table_name}")
        print("-" * 30)
        
        # Display columns
        for column in table.columns:
            column_info = f"  • {column.name} ({column.type})"
            if column.primary_key:
                column_info += " [PRIMARY KEY]"
            if column.foreign_keys:
                fk_info = ", ".join([f"{fk.column.table.name}.{fk.column.name}" 
                                   for fk in column.foreign_keys])
                column_info += f" [FK: {fk_info}]"
            if not column.nullable:
                column_info += " [NOT NULL]"
            
            print(column_info)

def demonstrate_relationships():
    """
    Demonstrate the relationships between tables.
    
    This function explains:
    - One-to-Many: Teacher -> Classes
    - Many-to-Many: Students <-> Classes
    - Foreign key constraints
    """
    print("\n🔗 Table Relationships:")
    print("=" * 50)
    
    print("\n1️⃣ One-to-Many Relationship:")
    print("   Teacher (1) -----> (Many) Classes")
    print("   - One teacher can teach multiple classes")
    print("   - Each class has exactly one teacher")
    print("   - Foreign key: classes.teacher_id -> teachers.id")
    
    print("\n2️⃣ Many-to-Many Relationship:")
    print("   Students (Many) <-----> (Many) Classes")
    print("   - One student can attend multiple classes")
    print("   - One class can have multiple students")
    print("   - Association table: class_students")
    print("   - Foreign keys: class_students.class_id -> classes.id")
    print("   - Foreign keys: class_students.student_id -> students.id")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Main execution block for the SQLAlchemy basics tutorial
    # This block:
    # 1. Creates the database schema
    # 2. Displays table information
    # 3. Explains relationships
    # 4. Provides next steps for learning
    print("🎓 SQLAlchemy Basics Tutorial - Core Concepts")
    print("=" * 60)
    
    # Create database schema
    create_database_schema()
    
    # Display table information
    display_table_info()
    
    # Demonstrate relationships
    demonstrate_relationships()
    
    print("\n🎯 Next Steps:")
    print("=" * 30)
    print("1. Run main.py to see ORM examples")
    print("2. Explore ZeqTech tutorials for advanced concepts")
    print("3. Practice with CRUD operations")
    print("4. Learn about query optimization")
    
    print("\n✅ Tutorial completed successfully!")
    print("💡 Key takeaways:")
    print("   - SQLAlchemy Core provides low-level database access")
    print("   - Metadata holds all table definitions")
    print("   - Foreign keys establish relationships")
    print("   - Association tables handle many-to-many relationships")
