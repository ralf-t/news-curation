"""Post models"""

from datetime import datetime
from news_curation.extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #use the author attribute to access post author details

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"