import os
import sys
from app.models.notification import Notification
from config import myconfig

FOLDER = myconfig.QUEUE_FOLDER

def create_file(notification):
    """Create a file containing the notification"""
    
    if not notification.is_valid():
        return False

    filename = notification.filename()
    
    try:
        fo = open(FOLDER + "/" + filename, "w")
        fo.write(notification.username() + ":" + notification.message + ":" + filename)
        fo.close()
        return True
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    
    return False

def delete_oldest_file(self):
    """Delete the oldest file"""
    x =2

def read_oldest_file(self):
    """Read the oldest file"""
    x = 2
