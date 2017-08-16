import sys
from datetime import datetime
from app.utils.file_manager import FileManager

class NotificationManager:
    def __init__(self, folder, date_format):
        self.folder = folder
        self.file_man = FileManager(folder)
        self.date_format = date_format
        
    def create_notification(self, username, message, light= 1, sound = 1):
        # Make sure all params are here
        if not username:
            return False
        if not message:
            return False
        
        timestamp = datetime.now()
        sent_at = timestamp.strftime(self.date_format)
        
        # create a file
        if self.file_man.create_notification(username, message, timestamp):
            return True
        
        # write screen
        
        # make sound
        
        # turn on light
        
        return False

        
