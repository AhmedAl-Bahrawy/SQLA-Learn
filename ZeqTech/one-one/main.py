import email
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

engine = create_engine('sqlite:///' + os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "database.db")
                       , echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# ----- One-to-One

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = relationship("Address", back_populates="user", uselist=False) #That make the relationship between User and His Address


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id')) #Store its user id
    user = relationship("User", back_populates="address") # Relationship between Address and user
    

user1 = User(name="Ahmed Albahrawy")
address1 = Address(email_address='ahmedalbahrawy-2010@hotmail.com', user=user1)

session.add(user1)
session.add(address1)
session.commit()



Base.metadata.create_all(engine)



print(address1.user.name)
print(user1.address.email_address)