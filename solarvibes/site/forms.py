from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

# WEBSITE FORMS
# Templates
class EmailForm(FlaskForm):
	email 	= StringField('Email', validators=[DataRequired(), Length(min=5, max=30, message=None), Email()])

class EmailAndTextForm(EmailForm):
  first_name = StringField('First Name', validators=[DataRequired(), Length(min=-1, max=30, message='Maximum characters: 30')])
  last_name = StringField('Last Name', validators=[DataRequired(), Length(min=-1, max=30, message='Maximum characters: 30')])
  email = StringField('Email', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
  country = StringField('Country', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
  landsize = StringField('Landsize(ha)', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
  msg = StringField('Message', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])

class ContactUsForm(FlaskForm):
  name 	= StringField(label='Fullname', validators=[DataRequired(), Length(min=3, max=30, message=None)])
  email = StringField('Email', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
