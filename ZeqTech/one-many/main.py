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

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)
    
    
class Address(BaseModel):
    __tablename__ = "address"
    
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship("User", back_populates="addresses")
    
    def __repr__(self):
        return "<Address(city='%s', state='%s', zip_code='%s')>" % (
            self.city,
            self.state,
            self.zip_code,
        )
    

class User(BaseModel):
    __tablename__ = "user"
    
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
     
    addresses = relationship("Address", back_populates="user")
    
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


user1 = User(
    name="John",
    fullname="John Doe",
    nickname="John",
)

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


session.add(user1)
session.add(address1)
session.commit()

user1.addresses.extend([address1, address2])
session.commit()


print(f"User {user1.name} has {len(user1.addresses)} addresses: {user1.addresses}, his main Address is {user1.addresses[0]}")