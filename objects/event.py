import datetime
import uuid

class Event:
    def __init__(self):
        return
    def __init__(self, title : str = None, description : str  = None, date : datetime.date  = None, artists : str  = None, location : str  = None, flyer_filename : str  = None, **kwargs):
        self.event_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        try:
            self.artists = [artist.strip() for artist in artists.split(',')] 
        except:
            pass
        self.date = date
        self.location = location
        self.flyer_filename = flyer_filename

    def update(self, title=None, description=None, date=None, artists=None, location=None, flyer_filename=None, **kwargs):
        if title: self.title = title
        if description: self.description = description
        try:
            if artists: self.artists = [artist.strip() for artist in artists.split(',')] 
        except:
            pass
        if date: self.date = date
        if location: self.location = location
        if flyer_filename: self.flyer_filename = flyer_filename

    event_id : str
    title : str
    description : str
    date : datetime.date
    artists : list
    location : str
    flyer_filename : str

    def __str__(self):
        return str(self.event_id) + ": " + str(self.title) + " " + str(self.flyer_filename)