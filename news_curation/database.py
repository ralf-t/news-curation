from .extensions import db

# Alias common SQLAlchemy names
Column = db.Column
relationship = db.relationship

class CRUDMixin(db.Model):
	pass

