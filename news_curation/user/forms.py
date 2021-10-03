from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from news_curation.user.models import User

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), 
													Length(2, 15, 'Firstname must be between 2 and 15 characters long.'),
													Regexp("^[a-zA-Z\-\']+$", message="Firstname must not include special characters.")])
	last_name = StringField('Last Name', validators=[DataRequired(), 
													Length(2, 15, 'Lastname must be between 2 and 15 characters long.'),
													Regexp("^[a-zA-Z\-\']+$", message="Lastname must not include special characters.")])
	username = StringField('Username', validators=[DataRequired(), 
												# ST: https://security.stackexchange.com/questions/46875/why-is-there-a-minimum-username-length
												Length(6, 20, 'Username must be between 6 and 20 characters long.'),
												Regexp('^[a-zA-Z0-9]+$', message="Username must not include special characters.")])
	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Register')

	# validation for duplicate username/email
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This username is taken. Please choose another one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email is already taken. Please choose another one.')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')