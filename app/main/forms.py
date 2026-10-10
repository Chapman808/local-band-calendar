from wtforms import SubmitField, TextAreaField, SelectField, DateField, validators
from flask_wtf import FlaskForm 
import wtforms

class AddEventForm(FlaskForm):
  #name = SelectField('Name', choices=('Eva', 'Zubee'))
  title = TextAreaField('title', [validators.input_required(), validators.length(max=50)])
  description = TextAreaField('description', [validators.optional(), validators.length(max=500)])
  date = DateField('date', widget=wtforms.widgets.DateInput())
  submit = SubmitField('Generate')