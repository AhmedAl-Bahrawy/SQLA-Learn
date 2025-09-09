from sqlalchemy.sql.functions import user
from models import Address, session, User
import random
from sqlalchemy import func

# List of names, ages, and emails

address1 = Address(
    city="New York",
    state="NY",
    zip_code="10001",
)

address2 = Address(
    city="San Francisco",
    state="CA",
    zip_code="94110",
)

address3 = Address(
    city="Los Angeles",
    state="CA",
    zip_code="90001",
)

user1 = User(
    first_name = "John",
    last_name = "Doe",
    addresses = [address1, address2],
)

user2 = User(
    first_name = "Jane",
    last_name = "Doe",
    addresses = [address1],
)

user3 = User(
    first_name = "Bob",
    last_name = "Smith",
)

session.add_all([user1, user2, user3, address1, address2, address3])
session.commit()


print(user1.addresses or "No Addresses")
print(user2.addresses or "No Addresses")
print(user3.addresses or "No Addresses")
print('='*50)
print()
print(address1.user or "No User")
print(address2.user or "No User")
print(address3.user or "No User")
print('='*50)
print()
# 4 Joins Main Types
# Inner Join
# Left Outer Join
# Right Outer Join
# Full Outer Join


# 1 - Inner Join
print("Inner Join:")
print(*session.query(User).join(Address).all(), sep="\n")
print('='*50)
print()

# 2 - Anti Inner Join
print("Anti Inner Join:")
print(*session.query(User, Address).join(Address, full=True).filter(User.addresses == None, Address.user_id == None).all(), sep="\n")
print('='*50)
print()

# 3 - Left Outer Join
print("Left Outer Join:")
print(*session.query(User, Address).outerjoin(Address).all(), sep="\n")
print('='*50)
print()

# 4 - Anti Left Outer Join
print("Anti Left Outer Join:")
print(*session.query(User, Address).outerjoin(Address, full=True).filter(User.addresses == None).all(), sep="\n")
print('='*50)
print()


# 5 - Right Outer Join
print("Right Outer Join:")
print(*session.query(User, Address).outerjoin(User).all(), sep="\n")
print('='*50)
print()

# 6 - Anto Right Outer 
print("Anti Right Outer Join:")
print(*session.query(User, Address).outerjoin(User, full=True).filter(Address.user_id == None).all(), sep="\n")
print('='*50)
print()

# 7 - Full Outer Join
print("Full Outer Join:")
print(*session.query(User, Address).outerjoin(User, full=True).all(), sep="\n")
print('='*50)
print()




# ------------------------------------------------- THE END -------------------------------------------------