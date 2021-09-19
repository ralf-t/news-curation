"""Factories to help in tests"""
from news_curation.database import db
from news_curation.user.models import User

from factory import Sequence, PostGenerationMethodCall
from factory.alchemy import SQLAlchemyModelFactory

class BaseFactory(SQLAlchemyModelFactory):
	"""Base factory"""

	class Meta:
		"""Factory configuration"""

		abstract = True
		sqlalchemy_session = db.session


class UserFactory(BaseFactory):
	"""User factory"""


	first_name= Sequence(lambda n: f"user")
	last_name= Sequence(lambda n: f"{n}")
	username= Sequence(lambda n: f"user{n}")
	email= Sequence(lambda n: f"user{n}@example.com")
	# TODO: set_password
	# password = PostGenerationMethodCall("set_password", "example")

	class Meta:
		"""Factory configuration"""

		model = User