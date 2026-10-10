from . import main
from .forms import AddEventForm, EditEventForm
from flask import make_response, render_template, redirect, url_for, request, session
import dao.dao as dao
import datetime


@main.route('/', methods=['GET'])
def index(requireActions : bool = None):
  event_id = request.args.get('event_id')
  events_today = dao.get_events_today()
  return render_template('index.html', events_today=events_today, event_id=event_id)

@main.route('/event', methods=['GET'])
def get_event(requireActions : bool = None):
  event_id = request.args.get('event_id')
  try:
    event = dao.get_event_by_id(event_id)
  except:
    event = None
  return render_template('event.html', event=event)

@main.route('/add_event', methods=['GET', 'POST'])
def form(requireActions : bool = None):
  form = AddEventForm()
  if form.validate_on_submit() and request.method == 'POST':
    event_data = form.data #add to form later
    print(event_data)
    title = event_data['title']
    description = event_data['description']
    date =  event_data['date']

    event_id = dao.add_event(title, description, date)
    return redirect(url_for('main.index', event_id=event_id)) 
    #return render_template('edit_profile.html', form=form, message=f"")
  return render_template('edit_profile.html', form=form, message="")

@main.route('/edit_event', methods=['GET', 'POST'])
def edit_form(requireActions : bool = None):
  form = EditEventForm(prev_title="test")
  event_id = request.args.get('event_id')
  if form.validate_on_submit():
    event_data = form.data #add to form later
    title = event_data['title']
    description = event_data['description']
    date =  event_data['date']

    event_id = dao.update_event(event_id, title, description, date)
    return redirect(url_for('main.index', event_id=event_id)) 
    #return render_template('edit_profile.html', form=form, message=f"")
  return render_template('edit_event.html', form=form, message="")

