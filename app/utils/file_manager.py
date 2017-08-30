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
        #print("I/O error({0}): {1}".format(errno,strerror))
        raise IOError
    except:
        #print("Unexpected error:", sys.exc_info()[0])
        raise

def count_files():
    """ Count the number of files in the queue folder excluding files starting with "." """
    return len([f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f[0] != '.'])
    
def delete_oldest_file():
    """Delete the oldest file"""
    filelist = [os.path.join(FOLDER, f) for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f[0] != '.']
    if len(filelist) > 0:
        oldest = min(filelist, key=lambda x: os.stat(x).st_mtime)
        try:
            os.remove(oldest)
        except:
            raise
        return True
    return False

def read_oldest_file():
    """Read the oldest file and return a notification"""
    filelist = [os.path.join(FOLDER, f) for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f[0] != '.']
    if len(filelist) > 0:
        oldest = min(filelist, key=lambda x: os.stat(x).st_mtime)

        try:
            with open(oldest) as oldest_file:
                notification = Notification.from_json(oldest_file.read())
                return notification
                
        except IOError as e:
            #errno, strerror = e.args
            #print("I/O error({0}): {1}".format(errno,strerror))
            #return None
            raise IOError
        except:
            #print("Unexpected error:", sys.exc_info()[0])
            #return None
            raise
    
    return None

