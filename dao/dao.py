import pickle
from datetime import date, timedelta
import uuid
import time 
import pandas as pd

def get_events():
  try:
    with open ('data/events.pkl', 'rb') as events:
      events = pickle.load(events)
      events = dict(events)
  except Exception as e:
    print("ERROR: Could not load events.pkl file from data")
    events = {}
  return events

def get_event_by_id(event_id : str):
  events = get_events()
  all_events = events.values()
  for event_set in all_events:
    if event_id in event_set:
        return event_set[event_id]
  raise ValueError
  

def get_events_today():
  events = get_events()
  print(events)
  if date.today() in events:
    print("found events today!")
    events_today = events[date.today()]
    #print(events_today.values())
    return events_today
  else: return None

def get_events_next_two_weeks():
  events = get_events()
  dates = pd.date_range(date.today(), date.today() + timedelta(weeks=2) ).tolist()
  output = {}
  for d in dates:
    d = d.to_pydatetime().date()
    if d not in events: continue
    output.update(events[d])
  return output

def store_flyer_image(image_file, event_id):
  file_extension = image_file.filename.split('.')[-1]
  with open(f'app/static/images/{event_id}.{file_extension}', 'wb') as f:
    f.write(image_file.read())

def add_event(data) -> None:
  event_id = str(uuid.uuid4())
  events = get_events()
  date = data['date']
  if date not in events: events[date] = {}
  events[date][event_id] = data
  with open ('data/events.pkl', 'wb') as events_file:
    pickle.dump(events, events_file)
  return event_id


