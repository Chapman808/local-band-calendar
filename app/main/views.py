from . import main
from .forms import AddEventForm, EditEventForm
from flask import make_response, render_template, redirect, url_for, request, session
import dao.dao as dao
import datetime
import os
import objects.event

@main.route('/', methods=['GET'])
def index(requireActions : bool = None):
  ref_event_id = request.args.get('event_id')
  events_today = dao.get_events_today()
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
    event = objects.event.Event(**form.data)
    if form.flyer.data:
       event.flyer_filename = dao.store_flyer_image(request.files[form.flyer.name], event.event_id)
    dao.add_event(event)
    return redirect(url_for('main.index', event_id=event.event_id)) 
  return render_template('add_event.html', form=form, message="")

@main.route('/edit_event', methods=['GET', 'POST'])
def edit_form(requireActions : bool = None):
  event_id = request.args.get('event_id')
  if(event_id):
    event = dao.get_event_by_id(event_id)
    form = EditEventForm(obj=event)
  else: return EditEventForm()
  if request.method == 'POST':
    if form.flyer.data:
      event.flyer_filename = dao.store_flyer_image(request.files[form.flyer.name], event.event_id)
    event.update(**form.data)
    dao.edit_event(event)
    return redirect(url_for('main.index', event_id=event_id)) 
    #return render_template('edit_profile.html', form=form, message=f"")
  return render_template('edit_event.html', form=form, message="")

