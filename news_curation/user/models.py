"""User models"""

from datetime import datetime
from news_curation.extensions import db, login_manager
from flask_login import UserMixin

# for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# relationship tables
user_interests = db.Table('user_interests',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
            )

saves = db.Table('saves',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
        )

class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(20), nullable=False)
        last_name = db.Column(db.String(20), nullable=False)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(60), nullable=False)
        profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
        

        # adds an 'invisible column' to Topic table named interested_user
        # which can be used to see user details that is interested in that topic ex.
        # for user in topic1.interested_user:
        #   print(user.username)
        topics_of_interest = db.relationship('Topic', secondary=user_interests,
                            backref=db.backref('interested_user'), lazy='dynamic')

        saved_posts = db.relationship('Post', secondary=saves,
                            backref=db.backref('saved_by'), lazy='dynamic')

        authored_posts = db.relationship('Post', backref='author', lazy=True)

        comments = db.relationship('Comment', backref='author', lazy=True)

        def __repr__(self):     #what will be printed out when we print this model
            return f"User('{self.first_name} {self.last_name}', '{self.username}', '{self.email}', '{self.profile_picture}')"

