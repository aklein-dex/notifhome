import sys
from datetime import datetime
from app.utils.file_manager import create_file
from app.models.user import User
from app.models.notification import Notification


def process_notification(user, message, light= 1, sound = 1):
    notification = Notification(user, message, datetime.now(), light, sound)
    
    if not notification.is_valid():
        return False
    
    # create a file
    if create_file(notification):
        return True
    
    # do a check if we are on the Omega2 or on a "real" computer
    # write on OLED screen
    
    # make sound
    
    # turn on light
    
    return False

    
