import sys
from app.models.user import User
from config import myconfig

USERS_FILE = myconfig.USERS_FILE

def login(user):
    """check if the param user matches one of the entries of the users file"""
    # Note: it opens and read the files everytime. Maybe we could read the file
    #       just once and save a list of users.
    if not user.is_valid():
        return False

    try:
        with open(USERS_FILE, 'r') as file:
            for line in file:
                split = line.rstrip().split(":")
                
                if len(split) < 2:
                    continue

                if user.matches(split[0], split[1]):
                    return True
    except IOError:
        raise IOError
    except:
        raise
        
    return False
