from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

# WEBSITE FORMS
# Templates
class EmailForm(FlaskForm):
	email 	= StringField('Email', validators=[DataRequired(), Length(min=5, max=30, message=None), Email()])

class EmailAndTextForm(EmailForm):
  first_name = TextAreaField('First Name', validators=[DataRequired(), Length(min=-1, max=30, message='Maximum characters: 30')])
  last_name = TextAreaField('Last Name', validators=[DataRequired(), Length(min=-1, max=30, message='Maximum characters: 30')])
  email = TextAreaField('Email', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
  country = TextAreaField('Country', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
  landsize = TextAreaField('Landsize', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])
  msg = TextAreaField('Message', validators=[DataRequired(), Length(min=-1, max=50, message='Maximum characters: 50')])

class ContactUsForm(EmailAndTextForm):
    name 	= StringField(label='Fullname', validators=[DataRequired(), Length(min=3, max=30, message=None)])
    phone 	= StringField('Phone', validators=[DataRequired(), Length(min=7, max=30, message=None)])
