from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

# ----- Database Config -----
engine = create_engine(
    'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"),
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# ----- Models -----
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # One-to-One (uselist=False)
    address = relationship("Address", back_populates="user", uselist=False)


class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="address")


# ----- Create Tables -----
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# ----- Insert Data -----
# user1 = User(name="Ahmed Albahrawy")
# address1 = Address(email_address="ahmedalbahrawy-2010@hotmail.com", user=user1)

# session.add(user1)
# session.add(address1)
# session.commit()

# ----- Test Output -----
# print(address1.user.name)          # should print: Ahmed Albahrawy
# print(user1.address.email_address) # should print: ahmedalbahrawy-2010@hotmail.co

user1 =  session.query(User).filter_by(name="Ahmed Albahrawy").all()



for u in user1:
    print(f"User: {u.name}, Address: {u.address.email_address}")


