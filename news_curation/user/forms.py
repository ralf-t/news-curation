from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from news_curation.user.models import User

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', 
		validators=[
			DataRequired(), 
			Length(min=2, max=15), 
			# Regexp('^([A-Z]*[a-z]+([ ]?[A-Za-z]*[\'-]?[A-Za-z]*)*.?)$', message='First name cannot contain numbers and special characters.')
			Regexp('^([A-Z]*[a-z]*([ ]?[A-Za-z]*[\'-]?[A-Za-z]*)*.?)$', message='First name cannot contain numbers and special characters.')
		], 
		render_kw={"placeholder": "First Name*",
					"meld:model.lazy": "first_name"})
	
	last_name = StringField('Last Name', validators=[
			DataRequired(), 
			Length(min=2, max=15),
			Regexp('^([A-Z]*[a-z]*([ ]?[A-Za-z]*[\'-]?[A-Za-z]*)*.?)$', message='Last name cannot contain numbers and special characters.')
		], 
		render_kw={"placeholder": "Last Name*",
					"meld:model.lazy": "last_name"})
	
	username = StringField('Username', validators=[
			DataRequired(), 
			Length(min=2, max=20, message='Username should be between 2 and 20 characters long.'),
			Regexp('^[A-Z0-9a-z\-._]+$', message='Username should only contain letters, numbers, dashes, periods, and underscores.')
		], 
		render_kw={"placeholder": "Username*",
					"meld:model.lazy": "username"})
	
	email = StringField('Email', validators=[
			DataRequired(), 
			Email()
		], 
		render_kw={"placeholder": "Email*",
					"meld:model.lazy": "email"})

	password = PasswordField('Password', validators=[DataRequired()], 
		render_kw={"placeholder": "Password*",
					"meld:model.lazy": "password"})
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], 
		render_kw={"placeholder": "Confirm Password*",
					"meld:model.lazy": "confirm_password"})

	submit = SubmitField('Register')

	# custom validations
	def validate_username(self, username):
		# validation for duplicate username
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This username is taken. Please choose another one.')

	def validate_email(self, email):
		#validation for duplicate email
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email is already taken. Please choose another one.')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	password = PasswordField('New Password', validators=[DataRequired()], 
		render_kw={"placeholder": "New Password",
					"meld:model.lazy": "password"})
	confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')], 
		render_kw={"placeholder": "Confirm New Password",
					"meld:model.lazy": "confirm_password"})

	submit = SubmitField('Save Changes')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('This username is taken. Please choose another one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('This email is already taken. Please choose another one.')