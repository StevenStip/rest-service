from datetime import datetime

class meeting(object):
    def __init__(self, location, created_by):
        self.created_time = datetime.utcnow()
        self.location = location
        self.created_by_user = created_by