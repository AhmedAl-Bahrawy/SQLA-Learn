from models import session, User
import random

# List of names, ages, and emails

names = ['Ahmed', 'Omar', 'Ali', 'Mohammed', 'Khalid', 'Belal']
ages = [30, 25, 20, 35, 40, 20]
emails = ['ahmed30@example.com', 'omar25@example.com', 'ali20@example.com', 'mohammed35@example.com', 'khalid40@example.com', 'belal20@example.com']


# Add users to the database by ziping the lists and ordering 
for name, age, email in zip(names, ages, emails):
    user = User(name=name, age=age, email=email)
    session.add(user)

session.commit()


# Add 20 random users to the database
for _ in range(20):
    user = User(name=random.choice(names), age=random.choice(ages), email=random.choice(emails))
    session.add(user)

session.commit()


# Filter all users by the normal ways

print(*session.query(User).all(), sep="\n")

print('='*50)
print()
print('='*50)

print(*(session.query(User).filter_by(age=20).all() or ["No users found"]), sep="\n")

print('='*50)
print()
print('='*50)

print(*(session.query(User).filter_by(name="Ahmed").all() or ["No users found"]), sep="\n")

print('='*50)
print()
print('='*50)

print(*(session.query(User).filter_by(name="Ahmed", age=20).all() or ["No users found"]), sep="\n")

print('='*50)
print()
print('='*50)


# Filter all users with conditions

print(*(session.query(User).filter(User.age >= 20).all() or ["No users found"]), sep="\n")

print('='*50)
print()
print('='*50)

print(*(session.query(User).filter(User.name == "Ahmed", User.age == 20).all() or ["No users found"]), sep="\n")

print('='*50)
print()
print('='*50)

# use Filter_by to filter the users

print(*(session.query(User).filter_by(age=20).all() or ["No users found"]), sep="\n")
print('='*50)
print()
print('='*50)
print(*(session.query(User).filter_by(name="Ahmed").all() or ["No users found"]), sep="\n")
print('='*50)
print()
print('='*50)
print(*(session.query(User).filter_by(name="Ahmed", age=20).all() or ["No users found"]), sep="\n")


# use Where to filter the users

print(*(session.query(User).where(User.age == 20).all() or ["No users found"]), sep="\n")
print('='*50)
print()
print('='*50)
print(*(session.query(User).where(User.name == "Ahmed").all() or ["No users found"]), sep="\n")
print('='*50)
print()
print('='*50)
print(*(session.query(User).where(User.name == "Ahmed", User.age == 20).all() or ["No users found"]), sep="\n")

# A quistion that i asked myself ----- what is the difference between filter and where?
# Answer:
# I do not know the answer yet, i will ask myself later.