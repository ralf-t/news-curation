from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import random
# from news_curation.classifier.utils import predict


class CommentForm(FlaskForm):
	content = TextAreaField('Content', validators=[DataRequired(), Length(min=1)])
	submit = SubmitField('Comment')

	# validation for duplicate username/email
	# def validate_content(self, content):
	# 	if predict(content.data):
	# 		raise ValidationError("Content is detected as fake.")
