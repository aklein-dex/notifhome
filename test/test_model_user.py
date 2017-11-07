#!/usr/bin/env python
#
# Unit tests for the User model.
#
# Run the tests from the root folder of this project:
#   python test/test_model_user.py
#
import sys
sys.path.append('.')
sys.path.append('app')

from datetime import datetime
from models.user import User

import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        self.username = "admin"
        self.password = "password"
        self.valid_user = User(self.username, self.password)

        
    def test_user_is_valid(self):
        '''Test a valid user.'''
        assert self.valid_user.is_valid()
    
    def test_user_is_invalid_without_name(self):
        '''Test username is mandatory.'''
        invalid_user = User(None, "password")
        assert not invalid_user.is_valid()
        invalid_user = User("", "password")
        assert not invalid_user.is_valid()
    
    def test_notification_is_invalid_without_msg(self):
        '''Test password is mandatory.'''
        invalid_user = User("admin", None)
        assert not invalid_user.is_valid()
        invalid_user = User("admin", "")
        assert not invalid_user.is_valid()
    
    def test_it_matches(self):
        assert self.valid_user.matches(self.username, self.password)

    def test_it_doesnt_matches(self):
        assert not self.valid_user.matches(self.username, "anotherPassword")
        assert not self.valid_user.matches(self.username, None)
        assert not self.valid_user.matches("anotherUser", self.password)
        assert not self.valid_user.matches(None, self.password)
        
if __name__ == '__main__':
    print unittest.main()
