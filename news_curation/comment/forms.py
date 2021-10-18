from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import random

class CommentForm(FlaskForm):
	content = TextAreaField('Content', validators=[DataRequired(), Length(min=1)])
	submit = SubmitField('Comment')

	# validation for duplicate username/email
	def validate_content(self, comment):
		if random.randint(0, 10) >= 5:
			raise ValidationError("Your comment does not seem to be reliable.")