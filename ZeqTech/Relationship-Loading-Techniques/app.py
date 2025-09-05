from models import session, User, Post
from sqlalchemy import func




user_1 = User(name="Uncle Ahmed Albahrawy", age=30)
session.add(user_1)
session.commit()

post = Post(title='Uncle', content="Hello Everyone I am you uncle", user_id=user_1.id)
session.add(post)
session.commit()


print(post.user_id)
print(session.query(User).where(User.id == post.user_id).first())




# ------------------------------------------------- THE END -------------------------------------------------