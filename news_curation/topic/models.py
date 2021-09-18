"""Topic models"""

from datetime import datetime
from news_curation.extensions import db

# relationship tables
topics = db.Table('topics',
        db.Column('topic_id', db.Integer, db.ForeignKey('topic.id')),
        db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
        )

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', secondary=topics,
                            backref=db.backref('topic'), lazy='dynamic')

    def __repr__(self):
        return f"Topic('{self.id}', '{self.topic}')"