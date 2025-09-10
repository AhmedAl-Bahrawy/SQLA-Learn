"""
SQLAlchemy Indexes Tutorial - Performance Optimization with Database Indexing

This module demonstrates various indexing strategies in SQLAlchemy to optimize
database query performance. Indexes are crucial for improving query speed,
especially on large datasets.

Key Concepts Covered:
- Single column indexes
- Composite indexes
- Unique indexes
- Deferred column loading
- Check constraints
- Performance optimization techniques

Author: ZeqTech Tutorial Series
License: MIT
"""

from sqlalchemy import (
    create_engine, Column, Integer, String, Index, CheckConstraint
)
from sqlalchemy.orm import declarative_base, deferred, sessionmaker

# =============================================================================
# DATABASE CONFIGURATION
# =============================================================================

# Create in-memory SQLite database for testing purposes
# In production, use persistent database: "sqlite:///database.db"
engine = create_engine("sqlite:///:memory:", echo=True)

# Create session factory and session instance
Session = sessionmaker(bind=engine)
session = Session()

# Create declarative base for model definitions
Base = declarative_base()

# =============================================================================
# BASE MODEL CLASS
# =============================================================================

class BaseModel(Base):
    """
    Abstract base model class that provides common functionality
    for all database models in this application.
    
    Features:
    - Abstract base class (cannot be instantiated directly)
    - Common primary key field (id)
    - Allows unmapped attributes for flexibility
    """
    __abstract__ = True
    __allow_unmapped__ = True
    
    # Primary key field - auto-incrementing integer
    id = Column(Integer, primary_key=True)

# =============================================================================
# USER MODEL WITH INDEXING EXAMPLES
# =============================================================================

class User(BaseModel):
    """
    User model demonstrating various SQLAlchemy indexing techniques.
    
    This model showcases:
    - Single column indexes for frequently queried fields
    - Composite indexes for multi-column queries
    - Unique indexes for data integrity
    - Deferred loading for performance optimization
    - Check constraints for data validation
    """
    __tablename__ = "users"

    # =====================================================================
    # COLUMN DEFINITIONS WITH INDEXING
    # =====================================================================
    
    # Single column index on name field
    # - index=True: Creates a B-tree index for fast lookups
    # - nullable=False: Ensures data integrity
    # - String(100): Limits length for performance and storage efficiency
    name = Column(String(100), index=True, nullable=False)
    
    # Deferred column loading for age field
    # - deferred(): Loads only when explicitly accessed
    # - group="demographic": Groups related deferred columns
    # - Reduces memory usage and initial query time
    age = deferred(Column(Integer), group="demographic")
    
    # Email field with unique constraint and index
    # - unique=True: Ensures email uniqueness across all records
    # - index=True: Creates index for fast email lookups
    # - group="private": Groups with other private/sensitive data
    # - String(120): Standard email length limit
    email = deferred(Column(String(120), unique=True, index=True, group="private"))
    
    # Password field (deferred for security and performance)
    # - deferred(): Never loaded unless explicitly requested
    # - group="private": Groups with other sensitive data
    # - String(200): Accommodates hashed passwords
    password = deferred(Column(String(200), group="private"))

    # =====================================================================
    # TABLE-LEVEL CONSTRAINTS AND INDEXES
    # =====================================================================
    
    __table_args__ = (
        # Composite index on name and email columns
        # - Useful for queries filtering by both name and email
        # - More efficient than separate indexes for multi-column queries
        Index("ix_users_name_email", "name", "email"),
        
        # Check constraint for data validation
        # - Ensures age is non-negative (business rule)
        # - Prevents invalid data at database level
        CheckConstraint("age >= 0", name="ck_users_age_nonnegative"),
    )

    def __repr__(self):
        """
        String representation of User object for debugging and logging.
        
        Returns:
            str: Formatted string representation of the user
        """
        return f"<User(name='{self.name}', age='{self.age}', email='{self.email}')>"

# =============================================================================
# DATABASE SCHEMA CREATION
# =============================================================================

def create_database_schema():
    """
    Create the database schema by dropping existing tables and creating new ones.
    
    This function ensures a clean database state for testing and demonstration.
    In production, use Alembic for database migrations instead.
    """
    # Drop all existing tables (for clean testing)
    Base.metadata.drop_all(engine)
    
    # Create all tables defined in the models
    Base.metadata.create_all(engine)
    
    print("✅ Database schema created successfully!")

# =============================================================================
# EXAMPLE USAGE AND TESTING
# =============================================================================

def demonstrate_indexing():
    """
    Demonstrate various indexing concepts with example data and queries.
    
    This function shows:
    - How to create users with different data
    - Performance benefits of indexes
    - Query optimization techniques
    """
    # Create sample users
    users_data = [
        {"name": "Ahmed Ali", "age": 30, "email": "ahmed@example.com", "password": "hashed123"},
        {"name": "Omar Hassan", "age": 25, "email": "omar@example.com", "password": "hashed456"},
        {"name": "Fatima Ahmed", "age": 28, "email": "fatima@example.com", "password": "hashed789"},
        {"name": "Mohammed Ali", "age": 35, "email": "mohammed@example.com", "password": "hashed101"},
    ]
    
    # Create user objects
    users = [User(**user_data) for user_data in users_data]
    
    # Add to session and commit
    session.add_all(users)
    session.commit()
    
    print("✅ Sample users created successfully!")
    
    # Demonstrate query performance with indexes
    print("\n🔍 Query Examples:")
    
    # Query by name (uses single column index)
    user_by_name = session.query(User).filter(User.name == "Ahmed Ali").first()
    print(f"User by name: {user_by_name}")
    
    # Query by email (uses unique index)
    user_by_email = session.query(User).filter(User.email == "omar@example.com").first()
    print(f"User by email: {user_by_email}")
    
    # Query by age (deferred column - loads on access)
    users_by_age = session.query(User).filter(User.age > 25).all()
    print(f"Users over 25: {len(users_by_age)} found")
    
    # Demonstrate composite index usage
    user_by_name_email = session.query(User).filter(
        User.name == "Fatima Ahmed",
        User.email == "fatima@example.com"
    ).first()
    print(f"User by name and email: {user_by_name_email}")

if __name__ == "__main__":
    # Main execution block for running the indexing demonstration
    # This block:
    # 1. Creates the database schema
    # 2. Demonstrates indexing concepts
    # 3. Shows query performance examples
    print("🚀 Starting SQLAlchemy Indexing Tutorial")
    print("=" * 50)
    
    # Create database schema
    create_database_schema()
    
    # Demonstrate indexing concepts
    demonstrate_indexing()
    
    print("\n✅ Tutorial completed successfully!")
    print("💡 Key takeaways:")
    print("   - Use indexes on frequently queried columns")
    print("   - Composite indexes for multi-column queries")
    print("   - Deferred loading for performance optimization")
    print("   - Check constraints for data validation")
