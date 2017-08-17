import sys
from app.models.user import User
from config import myconfig

USERS_FILE = myconfig.USERS_FILE

def login(user):
    """check if the param user matches one of the entries of the users file"""
    if not user.is_valid():
        return False

    with open(USERS_FILE, 'r') as file:
        for line in file:
            split = line.split(":")
            
            if len(split) < 2:
                continue
                
            if user.matches(split[0], split[1]):
                return True
    return False
