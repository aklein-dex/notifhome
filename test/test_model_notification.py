#!/usr/bin/env python
#
# Unit tests for the Notification model.
#
# Run the tests from the root folder of this project:
#   python test/test_model_notification.py
#
import sys
sys.path.append('.')
sys.path.append('app')

from datetime import datetime
from models.notification import Notification

import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        self.valid_notification = Notification("admin", "hello", datetime.now(), 1, 1)

    def test_notification_shortname(self):
        '''Test a valid notification.'''
        assert self.valid_notification.short_username(5) == "admin"
        assert self.valid_notification.short_username(9) == "admin"
        assert self.valid_notification.short_username(2) == "ad"
        assert self.valid_notification.short_username(-5) == "admin"
        
    def test_notification_is_valid(self):
        '''Test a valid notification.'''
        assert self.valid_notification.is_valid()
    
    def test_notification_is_invalid_without_name(self):
        '''Test name is mandatory.'''
        invalid_notification = Notification(None, "hello", datetime.now(), 1, 1)
        assert not invalid_notification.is_valid()
        invalid_notification = Notification("", "hello", datetime.now(), 1, 1)
        assert not invalid_notification.is_valid()
    
    def test_notification_is_invalid_without_msg(self):
        '''Test message is mandatory.'''
        invalid_notification = Notification("admin", None, datetime.now(), 1, 1)
        assert not invalid_notification.is_valid()
        invalid_notification = Notification("admin", "", datetime.now(), 1, 1)
        assert not invalid_notification.is_valid()

    def test_notification_is_invalid_without_sent_a(self):
        '''Test sent_at is mandatory.'''
        invalid_notification = Notification("admin", "hello", None, 1, 1)
        assert not invalid_notification.is_valid()

if __name__ == '__main__':
    print unittest.main()
