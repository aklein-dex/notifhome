import sys
from app.models.user import User

class Authz:
    def __init__(self, users_file):
        self.users_file = users_file
        
    def login(self, user):
        """Read the users file and see if the param user matches one of 
           the entry of the file
        """
        if not user.is_valid():
            return False

        with open(self.users_file, 'r') as file:
            for line in file:
                split = line.split(":")
                
                if len(split) < 2:
                    continue
                    
                if user.matches(split[0], split[1]):
                    return True
        return False
