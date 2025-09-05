import os
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


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
    posts = relationship("Post", backref="user", lazy='select')
    


    def __repr__(self):
        return "<User(name='%s', age='%s')>" % (
            self.name,
            self.age,
        )
        
class Post(BaseModel):
    __tablename__ = "posts"
    
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    def __repr__(self):
        return "<Post(title='%s', content='%s')>" % (
            self.title,
            self.content,
        )
    
    
    

        
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)