from app.models.user import User

class Notification:
    """A simple Notification class"""
    def __init__(self, user, message, sent_at, light = 1, sound = 1):
        self.user    = user
        self.message = message
        self.sound   = sound
        self.light   = light
        self.sent_at = sent_at

    def username(self):
        return self.user.username
        
    def short_username(self, max_size):
        if len(self.user.username) > max_size:
            return self.user.username[0:max_size-1]
        else:
            return self.user.username
        
    def is_valid(self):
        """Check if the attributes are valid"""
        if self.user.is_valid() and self.message and self.sent_at:
            return True
        return False

    def filename(self):
        """The filename is just the date"""
        return self.sent_at.strftime("%Y%m%d%H%M%S")

    def sent_at_formated(self, date_format):
        """Return the date the notification was sent to a specified format"""
        return self.sent_at.strftime(date_format)
