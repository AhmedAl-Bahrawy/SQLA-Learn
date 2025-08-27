from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///students.db', echo=True)
conn = engine.connect()


conn.execute(text("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)"))

conn.commit()


session = Session(engine)
session.execute(text("INSERT INTO students (name, age) VALUES ('John', 20)"))
session.commit()








