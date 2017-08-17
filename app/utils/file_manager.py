import os
import sys
from app.models.notification import Notification

class FileManager:
    def __init__(self, folder):
        self.folder = folder
        
    def create_file(self, notification):
        """Create a file containing the notification"""
        # Make sure all params are here
        if not notification.is_valid():
            return False

        filename = notification.filename()
		
        try:
            fo = open(self.folder + "/" + filename, "w")
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
