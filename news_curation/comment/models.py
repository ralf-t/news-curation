"""Comment models"""

from datetime import datetime, timezone
from news_curation.extensions import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    #use the author attribute to access post author details

    def __repr__(self):
        return f"Comment('{self.content}', '{self.created_at}')"