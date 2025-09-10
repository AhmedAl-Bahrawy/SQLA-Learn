"""
SQLAlchemy CRUD Operations Tutorial - Create, Read, Update, Delete

This module demonstrates the fundamental CRUD operations in SQLAlchemy ORM.
It covers creating, reading, updating, and deleting database records with
practical examples and best practices.

Key Concepts Covered:
- Creating new records (Create)
- Reading and querying data (Read)
- Updating existing records (Update)
- Session management
- Query filtering
- Batch operations
- Error handling

Author: ZeqTech Tutorial Series
License: MIT
"""

from models import User, session

# =============================================================================
# CREATE OPERATIONS
# =============================================================================

def demonstrate_create_operations():
    """
    Demonstrate various ways to create new records in the database.
    
    This function shows:
    - Individual record creation
    - Batch record creation
    - Session management
    - Commit operations
    """
    print("🚀 CREATE Operations Demo")
    print("=" * 50)
    
    # Method 1: Individual record creation
    print("\n1️⃣ Individual Record Creation:")
    print("-" * 40)
    
    # Create individual user objects
    user_1 = User(
        name='Ahmed Hassan',
        age=30,
        email="ahmed30@example.com",
        password='secure123'
    )
    user_2 = User(
        name='Omar Ali',
        age=25,
        email="omar25@example.com",
        password='secure456'
    )
    user_3 = User(
        name='Fatima Ahmed',
        age=20,
        email="fatima20@example.com",
        password='secure789'
    )
    
    # Add users to session individually
    session.add(user_1)
    session.add(user_2)
    session.add(user_3)
    
    # Commit changes to database
    session.commit()
    print("✅ Individual users created successfully!")
    
    # Method 2: Batch record creation
    print("\n2️⃣ Batch Record Creation:")
    print("-" * 40)
    
    # Create multiple user objects
    users_batch = [
        User(name='Mohammed Ali', age=35, email="mohammed35@example.com", password='secure101'),
        User(name='Khalid Hassan', age=40, email="khalid40@example.com", password='secure202'),
        User(name='Aisha Ahmed', age=22, email="aisha22@example.com", password='secure303'),
        User(name='Youssef Omar', age=28, email="youssef28@example.com", password='secure404'),
    ]
    
    # Add all users at once
    session.add_all(users_batch)
    session.commit()
    print("✅ Batch users created successfully!")

# =============================================================================
# READ OPERATIONS
# =============================================================================

def demonstrate_read_operations():
    """
    Demonstrate various ways to read and query data from the database.
    
    This function shows:
    - Retrieving all records
    - Filtering records
    - Using different query methods
    - Result processing
    """
    print("\n🔍 READ Operations Demo")
    print("=" * 50)
    
    # Query 1: Get all users
    print("\n1️⃣ All Users:")
    print("-" * 30)
    all_users = session.query(User).all()
    for user in all_users:
        print(f"   • {user}")
    
    # Query 2: Filter by specific criteria
    print("\n2️⃣ Users with age 20:")
    print("-" * 30)
    young_users = session.query(User).filter_by(age=20).all()
    for user in young_users:
        print(f"   • {user}")
    
    # Query 3: Get first user matching criteria
    print("\n3️⃣ First user with age 20:")
    print("-" * 30)
    first_young_user = session.query(User).filter_by(age=20).first()
    if first_young_user:
        print(f"   • {first_young_user}")
    else:
        print("   • No user found with age 20")
    
    # Query 4: Count records
    print("\n4️⃣ Total number of users:")
    print("-" * 30)
    total_users = session.query(User).count()
    print(f"   • Total users: {total_users}")
    
    # Query 5: Filter with conditions
    print("\n5️⃣ Users older than 25:")
    print("-" * 30)
    older_users = session.query(User).filter(User.age > 25).all()
    for user in older_users:
        print(f"   • {user}")

# =============================================================================
# UPDATE OPERATIONS
# =============================================================================

def demonstrate_update_operations():
    """
    Demonstrate various ways to update existing records in the database.
    
    This function shows:
    - Updating individual records
    - Batch updates
    - Field-specific updates
    - Session management for updates
    """
    print("\n✏️ UPDATE Operations Demo")
    print("=" * 50)
    
    # Update 1: Update a specific user
    print("\n1️⃣ Update Specific User:")
    print("-" * 30)
    
    # Find user to update
    user_to_update = session.query(User).filter_by(name='Ahmed Hassan').first()
    if user_to_update:
        print(f"   Before: {user_to_update}")
        
        # Update user's age
        user_to_update.age = 31
        user_to_update.email = "ahmed31@example.com"
        
        # Commit changes
        session.commit()
        print(f"   After: {user_to_update}")
    else:
        print("   • User not found")
    
    # Update 2: Batch update
    print("\n2️⃣ Batch Update:")
    print("-" * 30)
    
    # Update all users with age 20 to age 21
    users_to_update = session.query(User).filter_by(age=20).all()
    for user in users_to_update:
        user.age = 21
        print(f"   Updated: {user}")
    
    session.commit()
    print("   ✅ Batch update completed!")
    
    # Update 3: Update with conditions
    print("\n3️⃣ Conditional Update:")
    print("-" * 30)
    
    # Update users older than 30
    old_users = session.query(User).filter(User.age > 30).all()
    for user in old_users:
        user.age += 1  # Increment age by 1
        print(f"   Updated: {user}")
    
    session.commit()
    print("   ✅ Conditional update completed!")

# =============================================================================
# DELETE OPERATIONS
# =============================================================================

def demonstrate_delete_operations():
    """
    Demonstrate various ways to delete records from the database.
    
    This function shows:
    - Deleting individual records
    - Batch deletion
    - Conditional deletion
    - Session management for deletions
    """
    print("\n🗑️ DELETE Operations Demo")
    print("=" * 50)
    
    # Delete 1: Delete specific user
    print("\n1️⃣ Delete Specific User:")
    print("-" * 30)
    
    # Find user to delete
    user_to_delete = session.query(User).filter_by(name='Youssef Omar').first()
    if user_to_delete:
        print(f"   Deleting: {user_to_delete}")
        session.delete(user_to_delete)
        session.commit()
        print("   ✅ User deleted successfully!")
    else:
        print("   • User not found")
    
    # Delete 2: Delete with conditions
    print("\n2️⃣ Conditional Delete:")
    print("-" * 30)
    
    # Delete users with age 21
    users_to_delete = session.query(User).filter_by(age=21).all()
    for user in users_to_delete:
        print(f"   Deleting: {user}")
        session.delete(user)
    
    session.commit()
    print("   ✅ Conditional delete completed!")
    
    # Show remaining users
    print("\n3️⃣ Remaining Users:")
    print("-" * 30)
    remaining_users = session.query(User).all()
    for user in remaining_users:
        print(f"   • {user}")

# =============================================================================
# QUERY EXAMPLES AND BEST PRACTICES
# =============================================================================

def demonstrate_query_best_practices():
    """
    Demonstrate best practices for SQLAlchemy queries and operations.
    
    This function shows:
    - Efficient query patterns
    - Error handling
    - Session management
    - Performance considerations
    """
    print("\n💡 Query Best Practices Demo")
    print("=" * 50)
    
    # Best Practice 1: Use try-except for error handling
    print("\n1️⃣ Error Handling:")
    print("-" * 30)
    
    try:
        # Attempt to create a user with duplicate email
        duplicate_user = User(
            name='Test User',
            age=25,
            email="ahmed31@example.com",  # This email already exists
            password='test123'
        )
        session.add(duplicate_user)
        session.commit()
    except Exception as e:
        print(f"   ❌ Error occurred: {e}")
        session.rollback()
        print("   ✅ Transaction rolled back successfully")
    
    # Best Practice 2: Use context managers for sessions
    print("\n2️⃣ Session Management:")
    print("-" * 30)
    print("   • Always commit or rollback transactions")
    print("   • Use try-except blocks for error handling")
    print("   • Close sessions when done")
    
    # Best Practice 3: Efficient queries
    print("\n3️⃣ Efficient Queries:")
    print("-" * 30)
    
    # Use specific columns when possible
    user_names = session.query(User.name).all()
    print(f"   User names: {[name[0] for name in user_names]}")
    
    # Use limit for large datasets
    first_three_users = session.query(User).limit(3).all()
    print(f"   First 3 users: {len(first_three_users)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    Main execution block for the CRUD operations tutorial.
    
    This block:
    1. Demonstrates create operations
    2. Shows read operations
    3. Performs update operations
    4. Executes delete operations
    5. Shows best practices
    """
    print("🎓 SQLAlchemy CRUD Operations Tutorial")
    print("=" * 60)
    
    try:
        # Demonstrate all CRUD operations
        demonstrate_create_operations()
        demonstrate_read_operations()
        demonstrate_update_operations()
        demonstrate_delete_operations()
        demonstrate_query_best_practices()
        
        print("\n🎯 Learning Outcomes:")
        print("=" * 30)
        print("✅ Create new records in database")
        print("✅ Read and query data efficiently")
        print("✅ Update existing records")
        print("✅ Delete records safely")
        print("✅ Handle errors and transactions")
        print("✅ Use best practices for database operations")
        
        print("\n🚀 Next Steps:")
        print("=" * 20)
        print("1. Explore Filtering-Data tutorial")
        print("2. Learn about relationship operations")
        print("3. Study query optimization techniques")
        print("4. Practice with complex queries")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        session.rollback()
    finally:
        # Close session
        session.close()
        print("\n✅ Tutorial completed successfully!")
        print("💡 Key takeaways:")
        print("   - CRUD operations are fundamental to database management")
        print("   - Always handle errors and manage transactions properly")
        print("   - Use appropriate query methods for your needs")
        print("   - Batch operations are more efficient than individual ones")