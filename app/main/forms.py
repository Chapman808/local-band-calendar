from flask_wtf.form import _Auto
from wtforms import SubmitField, TextAreaField, SelectField, DateField, validators
from flask_wtf import FlaskForm 
import wtforms

class AddEventForm(FlaskForm):
  #name = SelectField('Name', choices=('Eva', 'Zubee'))
  title = TextAreaField('title', [validators.input_required(), validators.length(max=50)])
  description = TextAreaField('description', [validators.optional(), validators.length(max=500)])
  date = DateField('date', widget=wtforms.widgets.DateInput())
  submit = SubmitField('Generate')

class EditEventForm(FlaskForm):
  def __init__(self, prev_title, formdata=_Auto):
    super().__init__(formdata)
    self.prev_title = prev_title

  title = TextAreaField('title', [validators.input_required(), validators.length(max=50)])
  description = TextAreaField('description', [validators.optional(), validators.length(max=500)])
  date = DateField('date', widget=wtforms.widgets.DateInput())
  submit = SubmitField('Generate')