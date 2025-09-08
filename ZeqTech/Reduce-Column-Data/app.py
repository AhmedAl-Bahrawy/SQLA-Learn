from models import session, User
from sqlalchemy.orm import defer, undefer, load_only, undefer_group
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

# 1) Basic query (deferred columns not loaded until accessed)
users = session.query(User).all()
print("All users (age/email/password are deferred until accessed):")
print(*users, sep="\n")
    
    

print("-"*100)
print()
print('-'*100)

print("# Defer specific columns at query time (override mapper)\n")
# 2) Defer specific columns explicitly for this query
users = session.query(User).options(
    defer(User.age),   # ensure age is deferred
    defer(User.email)  # ensure email is deferred
).all()
print("Defer(User.age), Defer(User.email):")
print(*users, sep="\n")



print("-"*100)
print()
print('-'*100)

print("# Undefer specific columns at query time\n")
# 3) Undefer columns (force-load even if mapper marks them deferred)
users = session.query(User).options(
    undefer(User.age),
    undefer(User.email)
).all()
print("Undefer(User.age), Undefer(User.email):")
for u in users:
    # Accessing the attributes does not trigger a new query because they were loaded
    print(u.name, u.age, u.email)

print("-"*100)
print()
print('-'*100)

print("# Undefer an entire group\n")
# 4) Undefer a whole group defined in the mapper (see models.py groups)
users = session.query(User).options(
    undefer_group("private")  # loads email and password together
).all()
print("Undefer group 'private' (email, password):")
for u in users:
    print(u.name, u.email, "(password loaded)")

print("-"*100)
print()
print('-'*100)

print("# Load-only specific columns (loads just these, defers others)\n")
# 5) Load only a subset of columns. Non-listed columns are deferred
users = session.query(User).options(
    load_only(User.id, User.name)
).all()
print("load_only(id, name): age/email/password deferred")
for u in users:
    # name is loaded; accessing age triggers a deferred load
    print(u.id, u.name)

print("-"*100)
print()
print('-'*100)

print("# Combine ordering and deferred loading\n")
users = session.query(User).options(
    load_only(User.id, User.name)
).order_by(User.name).all()
print("Ordered by name with load_only(name):")
for u in users:
    print(u.name)