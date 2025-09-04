from models import session, User
import random
from sqlalchemy import func

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


# Trying the group_by method and usage of it 
# Here we had tryed the func method for the fist time

print(*session.query(User.age, func.count(User.id)).group_by(User.age).all(), sep='\n')


print('-'*50)


# ------------------------------------------------- THE END -------------------------------------------------