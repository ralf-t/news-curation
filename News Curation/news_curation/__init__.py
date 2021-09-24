from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5d141685cfea864ff75cc2b355882b09'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test_user:test@localhost:5432/newscuration_db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)	#for handling user logins
login_manager.login_view = 'login'	#handles logged-out users from accessing restricted pages
login_manager.login_message_category = 'info'	#handles logged-out users from accessing restricted pages

from news_curation import routes