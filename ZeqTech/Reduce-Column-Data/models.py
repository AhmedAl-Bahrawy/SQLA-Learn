import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, deferred, sessionmaker


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

    
    # Just all about using Deferred and defer usecases
    # But in real it is very helpful 
    # I love it 
    name = Column(String)
    # Group demographics are deferred together (example for group-based undefer)
    age = deferred(Column(Integer), group="demographic")
    # Sensitive/private data grouped for undefer_group example
    email = deferred(Column(String), group="private")
    password = deferred(Column(String), group="private")


    def __repr__(self):
        return "<User(name='%s', age='%s', email='%s')>" % (
            self.name,
            self.age,
            self.email,
        )
        
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)