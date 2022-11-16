from app import db
from app.models import User, Post

u1 = User(username='john', email='john@example.com')
print(u1)
db.session.add(u1)
db.session.commit()

u2 = User(username='susan', email='susan@example.com')
db.session.add(u2)
db.session.commit()

users = User.query.all()
print(users)

for u in users:
    print(u.id, u.username)