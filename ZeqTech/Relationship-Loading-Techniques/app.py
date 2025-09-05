from models import session, User, Post
from sqlalchemy import func



user = User(name="Uncle Ahmed Albahrawy", age=30)
session.add(user)
session.commit()

post = Post(title='Uncle', content="Hello Everyone I am you uncle", user_id=user.id)
session.add(post)
session.commit()



# ------------------------------------------------- THE END -------------------------------------------------