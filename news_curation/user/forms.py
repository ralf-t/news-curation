from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from news_curation.user.models import User

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', 
		validators=[
			DataRequired(), 
			Length(min=2, max=15), 
			Regexp('^[A-Za-z\'\-.]+$', message='First name cannot contain special characters.')
		], 
		render_kw={"placeholder": "First Name*"})
	
	last_name = StringField('Last Name', validators=[
			DataRequired(), 
			Length(min=2, max=15),
			Regexp('^[A-Za-z\'\-.]+$', message='Last name cannot contain special characters.')
		], 
		render_kw={"placeholder": "Last Name*"})
	
	username = StringField('Username', validators=[
			DataRequired(), 
			Length(min=2, max=20)
		], 
		render_kw={"placeholder": "Username*"})
	
	email = StringField('Email', validators=[
			DataRequired(), 
			Email()
		], 
		render_kw={"placeholder": "Email*"})

	password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password*"})
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password*"})

	submit = SubmitField('Register')

	# custom validations
	def validate_username(self, username):
		# validation for duplicate username
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This username is taken. Please choose another one.')
		
		#validation for invalid characters
		excluded_chars = "*?!^+%&/()=}][{$#<>,"
		for char in self.username.data:
			if char in excluded_chars:
				raise ValidationError(f"Character {char} is not allowed.")

	def validate_email(self, email):
		#validation for duplicate email
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email is already taken. Please choose another one.')

	# def special_char_username(self, username):
	# 	#validation for invalid characters
	# 	excluded_chars = " *?!'^+%&/()=}][{$#"
 #    	for char in self.username.data:
 #        	if char in excluded_chars:
 #            	raise ValidationError(f"Character {char} is not allowed in username.")

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')