import json

class Notification:
    """A simple Notification class"""
    def __init__(self, username, message, sent_at, light = 1, sound = 1):
        self.username = username
        self.message  = message
        self.sound    = sound
        self.light    = light
        self.sent_at  = sent_at
        
    def short_username(self, max_size):
        if max_size > 0 and len(self.username) > max_size:
            return self.username[0:max_size]
        else:
            return self.username
        
    def is_valid(self):
        """Check if the attributes are valid"""
        if self.username and len(self.username) > 0 and self.message and len(self.message) > 0 and self.sent_at:
            return True
        return False

    def filename(self):
        """The filename is just the date"""
        return self.sent_at.strftime("%Y%m%d%H%M%S")

    def sent_at_formated(self, date_format):
        """Return the date the notification was sent to a specified format"""
        return self.sent_at.strftime(date_format)
    
    def to_json(self):
        return json.dumps(self.__dict__, default=str)
                
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
