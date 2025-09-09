import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, deferred, sessionmaker, relationship
from sqlalchemy import ForeignKey



engine = create_engine(
    'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)
    
    

    

class User(BaseModel):
    __tablename__ = "user"
    
    first_name = Column(String)
    last_name = Column(String)
     
    addresses = relationship("Address", backref="user")
    
    def __repr__(self):
        return "<User(first_name='%s', last_name='%s')>" % (
            self.first_name,
            self.last_name,
        )
        
class Address(BaseModel):
    __tablename__ = "address"
    
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    def __repr__(self):
        return "<Address(city='%s', state='%s', zip_code='%s')>" % (
            self.city,
            self.state,
            self.zip_code,
        )
        
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)