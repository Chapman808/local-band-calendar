from . import main
from .forms import AddEventForm, EditEventForm
from flask import make_response, render_template, redirect, url_for, request, session
import dao.dao as dao
import datetime
import os

@main.route('/', methods=['GET'])
def index(requireActions : bool = None):
  ref_event_id = request.args.get('event_id')
  events_today = dao.get_events_today()
  print(events_today)
  events_next_two_weeks = dao.get_events_next_two_weeks()
  return render_template('index.html', events_today=events_today, events_next_two_weeks=events_next_two_weeks, ref_event_id=ref_event_id)

@main.route('/event', methods=['GET'])
def get_event(requireActions : bool = None):
  event_id = request.args.get('event_id')
  try:
    event = dao.get_event_by_id(event_id)
  except:
    event = None
  return render_template('event.html', event_id=event_id, event=event)

@main.route('/add_event', methods=['GET', 'POST'])
def form(requireActions : bool = None):
  form = AddEventForm()
  if form.validate_on_submit() and request.method == 'POST':
    event_data = form.data
    title = event_data['title']
    #try:
    #  form.data['artists'] = [artist.strip() for artist in event_data['artists'].split(',')]
    #except Exception as e:
    #  print(e)
    #  return render_template('add_event.html', form=form, message="Failed to parse artist list.")

    flyer_object = form.data['flyer']
    event_data['file_extension'] = form.data['flyer'].filename.split(".")[-1]
    event_data['flyer'] = 'tmp'
    #print(event_data)
    event_id = dao.add_event(event_data)
    if form.flyer.data:
      dao.store_flyer_image(request.files[form.flyer.name], event_id)

    return redirect(url_for('main.index', event_id=event_id)) 
    #return render_template('edit_profile.html', form=form, message=f"")
  return render_template('add_event.html', form=form, message="")

@main.route('/edit_event', methods=['GET', 'POST'])
def edit_form(requireActions : bool = None):
  event_id = request.args.get('event_id')
  if(event_id):
    event = dao.get_event_by_id(event_id)
    form = EditEventForm(obj=event_id)
  else: form = EditEventForm()
  if form.validate_on_submit():
    form.populate_obj()
    event_data = form.data #add to form later
    title = event_data['title']
    description = event_data['description']
    date =  event_data['date']

    event_id = dao.update_event(event_id, event)
    return redirect(url_for('main.index', event_id=event_id)) 
    #return render_template('edit_profile.html', form=form, message=f"")
  return render_template('edit_event.html', form=form, message="")

