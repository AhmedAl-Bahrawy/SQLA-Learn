from models import User, session



# ------- Create -------

user_1 = User(name='Ahmed', age=30, email="ahmed30@example.com", password='123456')
user_2 = User(name='Omar', age=25, email="omar25@example.com", password='123456')
user_3 = User(name='Ali', age=20, email="ali20@example.com", password='123456')


# add by traditinal way
session.add(user_1)
session.add(user_2)
session.add(user_3)
session.commit()


# or 

user_4 = User(name='Mohammed', age=35, email="mohammed35@example.com", password='123456')
user_5 = User(name='Khalid', age=40, email="khalid40@example.com", password='123456')
user_6 = User(name='Belal', age=20, email="ali20@example.com", password='123456')

# or add by this prettiy way
session.add_all([user_4, user_5, user_6])
session.commit()

# ------- Read -------

# collect all users in a list and unlink the users form the list by the way I jsut learned now
print(*session.query(User).all(), sep='\n')

print('='*50)
print()
print('='*50)

# Filter any user and get just users with the value in the filter_by method 
print(*session.query(User).filter_by(age=20).all(), sep='\n') # must output 2 users


print('='*50)
print()
print('='*50)

#  Filter any user and get just first user with the vaulue in the filter method
print(session.query(User).filter_by(age=20).first()) # must output 1 user

print('='*50)
print()
print('='*50)

# ------- Update -------

user = session.query(User).filter_by(age=20).first()
user.age = 35
session.commit()
print(user)