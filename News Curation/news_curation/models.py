from datetime import datetime
from news_curation import db, login_manager
from flask_login import UserMixin

# secondary table for User and Topic model
# Shows which users are interested in a certain topic 
user_interests = db.Table('user_interests',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
            )

# table for saved posts
saves = db.Table('saves',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
        )

#for user login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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

        def __repr__(self):     #what will be printed out when we print this model
            return f"User('{self.first_name} {self.last_name}', '{self.username}', '{self.email}', '{self.profile_picture}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #use the author attribute to access post author details

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"Topic('{self.id}', '{self.topic}')"
