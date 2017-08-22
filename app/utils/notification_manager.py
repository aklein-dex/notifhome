import sys
import platform
from datetime import datetime
from app.utils.file_manager import create_file
from app.utils.screen_manager import print_screen, init_screen
from app.models.user import User
from app.models.notification import Notification


def process_notification(user, message, light= 1, sound = 1):
    success = False
    notification = Notification(user, message, datetime.now(), light, sound)
    
    if not notification.is_valid():
        return False
    
    # create all type of notifications
    if create_file(notification):
        
        if is_omega2():
            # write on OLED screen
            print_screen(notification)
            # make sound
        
            # turn on light
            success = True
        else:
            success = True
    
    return success

def init_hardware():
    init_screen()
    # init_sound
    # init_light
    
    
def is_omega2():
    """ Check if the current machine is an Omega2.
        I couldn't find any other way that is 100% accurate.
    """
    return platform.uname()[4] == 'mips'
        
