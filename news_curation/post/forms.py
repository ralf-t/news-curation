from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	topics = SelectField('Topics', coerce=int, validators=[DataRequired()]) #dropdown options are defined in routes.py

	add_topic = SubmitField('Add Tag')
	submit = SubmitField('Post')