import sys
from datetime import datetime
from app.utils.file_manager import FileManager
from app.models.user import User
from app.models.notification import Notification

class NotificationManager:
    def __init__(self, folder, date_format):
        self.folder = folder
        # pas besoin de creer une instance file_manager
        self.file_manager = FileManager(folder)
        self.date_format = date_format
        
    def build_notification(self, user, message, light= 1, sound = 1):
        return Notification(user, message, datetime.now(), light, sound)
        

    def process_notification(self, user, message, light= 1, sound = 1):
        notification = self.build_notification(user, message, light, sound)
        
        if not notification.is_valid():
            return False
        
        # create a file
        if self.file_manager.create_file(notification):
            return True
        
        # write screen
        
        # make sound
        
        # turn on light
        
        return False

        
