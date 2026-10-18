import re

from flask_wtf.form import _Auto
from wtforms import SubmitField, TextAreaField, SelectField, DateField, FieldList, FileField, StringField, validators, SelectMultipleField
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
import wtforms

class AddEventForm(FlaskForm):
  #name = SelectField('Name', choices=('Eva', 'Zubee'))
  title = StringField('title', [validators.input_required(), validators.length(max=50)])
  location = StringField('location', [validators.length(max=50)])
  description = TextAreaField('description', [validators.optional(), validators.length(max=500)])
  artists = StringField('artists', description='Note: enter Artists as a comma-separated list')
  date = DateField('date', widget=wtforms.widgets.DateInput())
  flyer = FileField('flyer', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

  submit = SubmitField('Generate')

class EditEventForm(FlaskForm):
  title = StringField('title', [validators.length(max=50)])
  location = StringField('location', [validators.length(max=50)])
  description = TextAreaField('description', [validators.optional(), validators.length(max=2000)])
  artists = TextAreaField('artists', description='Note: enter Artists as a comma-separated list')
  date = DateField('date', widget=wtforms.widgets.DateInput())
  flyer = FileField('flyer', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
  
  submit = SubmitField('Generate')