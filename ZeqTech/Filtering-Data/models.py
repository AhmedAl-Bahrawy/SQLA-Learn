import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


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
    __tablename__ = "users"

    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    password = Column(String)


    def __repr__(self):
        return "<User(name='%s', age='%s', email='%s')>" % (
            self.name,
            self.age,
            self.email,
        )
        
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)