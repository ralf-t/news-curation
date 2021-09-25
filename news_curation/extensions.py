"""Flask extensions initialized in app factory (see __init__.py)"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'user.login'	#handles logged-out users from accessing restricted pages
login_manager.login_message_category = 'info'	#handles logged-out users from accessing restricted pages

bcrypt = Bcrypt()