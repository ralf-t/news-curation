from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import random

class CommentForm(FlaskForm):
	content = StringField('Username', validators=[DataRequired(), Length(min=1)])
	submit = SubmitField('Submit')

	# validation for duplicate username/email
	def validate_content(self, comment):
        if random.randint(0, 10) >= 5:
            raise ValidationError("Your comment does not seem to be reliable.")