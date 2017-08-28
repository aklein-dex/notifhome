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
        fo.write(notification.to_json())
        fo.close()
        return True
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    
    return False

def count_files():
    """ Count the number of files in the queue folder excluding files starting with "." """
    return len([f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f[0] != '.'])
    
def delete_oldest_file():
    """Delete the oldest file"""
    if count_files() > 0:
        x =2
        # rm file

def read_oldest_file():
    """Read the oldest file and return a notification"""
    files = sorted(os.listdir(FOLDER), key=os.path.getctime)
    oldest = files[0]
    

