import pickle
import datetime
import uuid
import time 

def get_events():
  try:
    with open ('data/events.pkl', 'rb') as events:
      events = pickle.load(events)
      events = dict(events)
  except Exception as e:
    print("ERROR: Could not load events.pkl file from data")
    raise e
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
  if datetime.date.today() in events:
    events_today = events[datetime.date.today()]
    #print(events_today.values())
    return events_today
  else: return None




def add_event(title : str, description : str, date : datetime.datetime) -> None:
  event_id = str(uuid.uuid4())
  try:
    events = get_events()
  except Exception as e:
    print(e)
    print('could not load events. Initializing new events file')
    events = {}

  if date not in events: events[date] = {}
  events[date][event_id] = {'title' : title, 'description' : description, 'date' : date, 'event_id' : event_id}
  with open ('data/events.pkl', 'wb') as events_file:
    pickle.dump(events, events_file)
  return event_id

