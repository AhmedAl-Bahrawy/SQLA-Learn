import os
from sqlalchemy import (
    create_engine, Column, Integer, String, Index, UniqueConstraint, CheckConstraint
)
from sqlalchemy.orm import declarative_base, deferred, sessionmaker

# Database in memory (for testing)
engine = create_engine("sqlite:///:memory:")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Base model
class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)


class User(BaseModel):
    __tablename__ = "users"

    # Here We learned How to use Indexing
    # Columns
    name = Column(String(100), index=True, nullable=False)   # single index + length + not null
    age = deferred(Column(Integer), group="demographic")     # deferred for less memory
    email = deferred(Column(String(120), unique=True, index=True, group="private"))  # unique + index
    password = deferred(Column(String(200), group="private")) # deferred (load on demand)

    # Table-level constraints / indexes
    __table_args__ = (
        Index("ix_users_name_email", "name", "email"),       # composite index
        CheckConstraint("age >= 0", name="ck_users_age_nonnegative"),  # sanity check
    )

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}', email='{self.email}')>"


# Recreate schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
