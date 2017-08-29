import sys
import platform
import logging
from datetime import datetime
from app.utils.file_manager import create_file, read_oldest_file, delete_oldest_file
from app.models.user import User
from app.models.notification import Notification
import logging

# Check if the current machine is an Omega2. I couldn't find any other way that is 100% accurate.
if platform.uname()[4] == 'mips':
    logging.info('Platform is Omega2')
    is_omega2 = True
    from app.utils.screen_manager import print_screen, init_screen
else:
    is_omega2 = False
    logging.info("Platform is not Omega2")

def process_notification(user, message, light= 1, sound = 1):
    success = False
    notification = Notification(user.username, message, datetime.now(), light, sound)
    
    if not notification.is_valid():
        return False
    
    # create all type of notifications
    if create_file(notification):
        
        if is_omega2:
            # Print on screen only if this is the first notification
            if count_files() == 1:
                print_screen(notification)
            
            # make sound
        
            # turn on light
            success = True
        else:
            success = True
    else:
        logging.warning('Failed creating notification')
        success = False
    
    return success

def read_notification():
    notification = read_oldest_file()
    return notification
    
def delete_notification():
    deleted = delete_oldest_file()
    if is_omega2:
        #TODO clear screen
        # print on the screen the oldest following notif
        notification = read_oldest_file()
        if notification:
            print_screen(notification)
    return deleted

def init_hardware():
    initialized = True
    
    if is_omega2:
        initialized = init_screen()
        
        if initialized:
            # initialized = init_sound
            x = 2
            if initialized:
                # initialized = init_light
                x = 2
    
    return initialized

