"""Database file containing flask-sqlalchemy db object & base classes for convenience"""

from .extensions import db

# Alias common SQLAlchemy names
Column = db.Column
relationship = db.relationship

class PkModel(db.Model):
    """Base class for general tables"""

    __abstract__ = True
    id = Column(db.Integer, primary_key=True)
    