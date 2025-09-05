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



session.add_all(
    [
        User(
            name = f"User {y}",
            age = (y/2+1)*((1/2) * y),
            posts = [
                Post(
                    title = f'This is the title for {y * 10 + x}',
                    content = f'This is the content for {y * 10 + x}',
                ) for x in range(50)
            ],
        ) for y in range(10_000)
    ]
)
session.commit()


#print(*session.query(User).all(), sep='\n')
print('-'*100)
print(*session.query(User).where(Post.user_id == User.id).all(), sep='\n')
print('-'*100)
print(*session.query(User.name, func.count(Post.id)).join(Post).group_by(User).all(), sep='\n')


#print('-'*100) 
#print(*((user.name, count) for user, count in session.query(User, func.count(Post.id)).join(Post).group_by(User.id).all()), sep='\n')
#print('-'*100)
# ------------------------------------------------- THE END -------------------------------------------------