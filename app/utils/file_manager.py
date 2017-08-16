import os
import sys

class FileManager:
    def __init__(self, folder):
        self.folder = folder
        
    def create_notification(self, username, message, timestamp):
        """Create a file containing the notification"""
        # Make sure all params are here
        if not username:
            return False
        if not message:
            return False
        if not timestamp:
            return False

        # The filename is just the date
        filename = timestamp.strftime("%Y%m%d%H%M%S")
		
        try:
            fo = open(self.folder + "/" + filename, "w")
            fo.write(username + ":" + message + ":" + filename)
            fo.close()
            return True
        except IOError as e:
            errno, strerror = e.args
            print("I/O error({0}): {1}".format(errno,strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        
        return False
	
    def delete_notification(self):
        """Delete the oldest file"""
        x =2
    
    def read_notification(self):
        """Read the oldest file"""
        x = 2
