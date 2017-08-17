from app.models.user import User

class Notification:
    """A simple user class"""
    def __init__(self, user, message, sent_at, light = 1, sound = 1):
        self.user    = user
        self.message = message
        self.sound   = sound
        self.light   = light
        self.sent_at = sent_at

    def username(self):
        return self.user.username
        
    def is_valid(self):
        if self.user.is_valid() and self.message and self.sent_at:
            return True
        return False

    def filename(self):
        """The filename is just the date"""
        return self.sent_at.strftime("%Y%m%d%H%M%S")
