"""
Test cases for NeuralNine basics tutorial.

This module tests the fundamental SQLAlchemy Core concepts
demonstrated in the basics.py tutorial.
"""

import pytest
import os
import tempfile
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import sessionmaker

# Import the models from the tutorial
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'NeuralNine'))

class TestSQLAlchemyBasics:
    """Test cases for SQLAlchemy basics tutorial."""
    
    def setup_method(self):
        """Set up test database and metadata."""
        # Create temporary database file
        self.temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.temp_db.close()
        
        # Create engine with temporary database
        self.engine = create_engine(f'sqlite:///{self.temp_db.name}', echo=False)
        
        # Create metadata
        self.meta = MetaData()
        
        # Define tables (same as in basics.py)
        self.students = Table(
            'students', self.meta,
            Column('id', Integer, primary_key=True),
            Column('name', String, nullable=False),
            Column('age', Integer, nullable=False)
        )
        
        self.teachers = Table(
            'teachers', self.meta,
            Column('id', Integer, primary_key=True),
            Column('name', String, nullable=False),
            Column('age', Integer, nullable=False),
            Column('subject', String, nullable=False),
            Column('phone_num', String, nullable=True)
        )
        
        self.classes = Table(
            'classes', self.meta,
            Column('id', Integer, primary_key=True),
            Column('start_time', Time, nullable=True),
            Column('teacher_id', Integer, ForeignKey('teachers.id'))
        )
        
        self.class_students = Table(
            'class_students', self.meta,
            Column('class_id', Integer, ForeignKey('classes.id')),
            Column('student_id', Integer, ForeignKey('students.id'))
        )
        
        # Create all tables
        self.meta.create_all(self.engine)
    
    def teardown_method(self):
        """Clean up test database."""
        # Remove temporary database file
        if os.path.exists(self.temp_db.name):
            os.unlink(self.temp_db.name)
    
    def test_table_creation(self):
        """Test that tables are created successfully."""
        # Check that all tables exist
        inspector = self.engine.inspect()
        table_names = inspector.get_table_names()
        
        assert 'students' in table_names
        assert 'teachers' in table_names
        assert 'classes' in table_names
        assert 'class_students' in table_names
    
    def test_students_table_structure(self):
        """Test students table structure."""
        inspector = self.engine.inspect()
        columns = inspector.get_columns('students')
        
        # Check column names and types
        column_names = [col['name'] for col in columns]
        assert 'id' in column_names
        assert 'name' in column_names
        assert 'age' in column_names
        
        # Check primary key
        pk_columns = inspector.get_pk_constraint('students')['constrained_columns']
        assert 'id' in pk_columns
    
    def test_teachers_table_structure(self):
        """Test teachers table structure."""
        inspector = self.engine.inspect()
        columns = inspector.get_columns('teachers')
        
        # Check column names
        column_names = [col['name'] for col in columns]
        assert 'id' in column_names
        assert 'name' in column_names
        assert 'age' in column_names
        assert 'subject' in column_names
        assert 'phone_num' in column_names
    
    def test_classes_table_structure(self):
        """Test classes table structure."""
        inspector = self.engine.inspect()
        columns = inspector.get_columns('classes')
        
        # Check column names
        column_names = [col['name'] for col in columns]
        assert 'id' in column_names
        assert 'start_time' in column_names
        assert 'teacher_id' in column_names
    
    def test_foreign_key_relationships(self):
        """Test foreign key relationships."""
        inspector = self.engine.inspect()
        
        # Check foreign keys in classes table
        fks = inspector.get_foreign_keys('classes')
        assert len(fks) == 1
        assert fks[0]['referred_table'] == 'teachers'
        assert 'teacher_id' in fks[0]['constrained_columns']
        
        # Check foreign keys in class_students table
        fks = inspector.get_foreign_keys('class_students')
        assert len(fks) == 2
        
        referred_tables = [fk['referred_table'] for fk in fks]
        assert 'classes' in referred_tables
        assert 'students' in referred_tables
    
    def test_data_insertion_and_retrieval(self):
        """Test inserting and retrieving data."""
        # Insert test data
        with self.engine.connect() as conn:
            # Insert teacher
            teacher_result = conn.execute(
                self.teachers.insert().values(
                    name="Test Teacher",
                    age=30,
                    subject="Mathematics",
                    phone_num="1234567890"
                )
            )
            teacher_id = teacher_result.inserted_primary_key[0]
            
            # Insert student
            student_result = conn.execute(
                self.students.insert().values(
                    name="Test Student",
                    age=20
                )
            )
            student_id = student_result.inserted_primary_key[0]
            
            # Insert class
            class_result = conn.execute(
                self.classes.insert().values(
                    start_time="10:00:00",
                    teacher_id=teacher_id
                )
            )
            class_id = class_result.inserted_primary_key[0]
            
            # Insert class-student relationship
            conn.execute(
                self.class_students.insert().values(
                    class_id=class_id,
                    student_id=student_id
                )
            )
            
            conn.commit()
        
        # Verify data was inserted
        with self.engine.connect() as conn:
            # Check teacher
            teacher_result = conn.execute(
                self.teachers.select().where(self.teachers.c.id == teacher_id)
            ).fetchone()
            assert teacher_result is not None
            assert teacher_result.name == "Test Teacher"
            assert teacher_result.subject == "Mathematics"
            
            # Check student
            student_result = conn.execute(
                self.students.select().where(self.students.c.id == student_id)
            ).fetchone()
            assert student_result is not None
            assert student_result.name == "Test Student"
            assert student_result.age == 20
            
            # Check class
            class_result = conn.execute(
                self.classes.select().where(self.classes.c.id == class_id)
            ).fetchone()
            assert class_result is not None
            assert class_result.teacher_id == teacher_id
            
            # Check relationship
            relationship_result = conn.execute(
                self.class_students.select().where(
                    (self.class_students.c.class_id == class_id) &
                    (self.class_students.c.student_id == student_id)
                )
            ).fetchone()
            assert relationship_result is not None

if __name__ == "__main__":
    pytest.main([__file__])
