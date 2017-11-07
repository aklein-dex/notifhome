#!/usr/bin/env python
#
# Integration tests for Notifhome.
#
# Run the tests from the root folder of this project:
#   python test/test_notifhome.py
#
# Make sure the username and password in the setUp function
# exist otherwise some tests will fail.
#
#
import sys
# Run the test from the root folder, so have to append it otherwise
# it will not find config.
sys.path.append('.')
sys.path.append('lib')
sys.path.append('app')

from datetime import datetime
from bottle import Bottle

import controllers.application_controller as controller

import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        from webtest import TestApp
        from bottle import TEMPLATE_PATH
        TEMPLATE_PATH.insert(0, '../')
        self.app = controller.build_application()
        self.harness = TestApp(self.app)
        self.username = "admin"
        self.password = "123456"
        self.wrong_password = "wrong-password"

    def test_index(self):
        '''Test of Index page.'''
        results = self.harness.get('/')
        assert results.status_int == 200
        self.assertIn('Notifhome', results.body)
        
    def test_jquery(self):
        '''Make sure the jquery library is accessible.'''
        results = self.harness.get('/public/jquery.min.js')
        assert results.status_int == 200

    def test_notification_life_cycle(self):
        '''Notification life cycle'''
        message = "Test " + datetime.now().strftime("%Y%m%d%H%M%S")
        
        # 1: Create notification
        results = self.harness.post('/notification',
                {'message': message,
                    'light': 1,
                    'sound': 1,
                    'password': self.password,
                    'username': self.username,
                })
        assert results.status_int == 200
        
        # 2: Verify that we can read the notification
        results = self.harness.get('/notification',
                {'password': self.password,
                    'username': self.username,
                })
        assert results.status_int == 200
        self.assertIn(message, results.body)
        self.assertIn('\\"sound\\": \\"1\\"', results.body)
        self.assertIn('\\"light\\": \\"1\\"', results.body)
        self.assertIn('admin', results.body)
        
        # 3: Delete the notification
        results = self.harness.delete('/notification',
                {'password': self.password,
                    'username': self.username,
                })
        assert results.status_int == 200
        self.assertIn('Notification deleted', results.body)
        
        # 4: Verify that the notification doesn't exist anymore
        results = self.harness.get('/notification',
                {'password': self.password,
                    'username': self.username,
                })
        assert results.status_int == 200
        self.assertNotIn(message, results.body)
        
    def test_message_is_mandatory(self):
        '''Parameter message is not sent so the notification is invalid.'''
        
        results = self.harness.post('/notification',
                {'light': 1,
                    'sound': 1,
                    'password': self.password,
                    'username': self.username,
                }, expect_errors=True)
        
        assert results.status_int == 400
        
    def test_cant_create_notification(self):
        '''A user needs to be authenticated to create a notification.'''
        
        results = self.harness.post('/notification',
                {'message': "hello",
                    'light': 1,
                    'sound': 1,
                    'password': self.wrong_password,
                    'username': self.username,
                }, expect_errors=True)
        
        assert results.status_int == 401
        
        
    def test_cant_read_notification(self):
        '''A user needs to be authenticated to read a notification.'''
        
        results = self.harness.get('/notification',
                {'password': self.wrong_password,
                }, expect_errors=True)
                
        assert results.status_int == 403
    
    def test_cant_delete_notification(self):
        '''A user needs to be authenticated to delete a notification.'''
        
        results = self.harness.delete('/notification',
                {'password': self.wrong_password,
                    'username': self.username,
                }, expect_errors=True)
                
        assert results.status_int == 401
        
if __name__ == '__main__':
    print unittest.main()
