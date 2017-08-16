import sys
import bottle
from app.models.user import User
from datetime import datetime

class Authz:
    def __init__(self, users_file):
        self.users_file       = users_file
        
    def login(self, username, password):
        # Read the users file
        with open(self.users_file, 'r')  as file:
            for line in file:
                split = line.split(":")
                if split[0] == username and split[1] == password:
                    return True
        return False
