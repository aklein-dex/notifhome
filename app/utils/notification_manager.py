import sys
import platform
import logging
from utils.file_manager import create_file, read_oldest_file, delete_oldest_file
from models.notification import Notification
from config import myconfig
import logging

# Check if the current machine is an Omega2. I couldn't find any other way that is 100% accurate.
if platform.uname()[4] == 'mips':
    logging.info('Platform is Omega2')
    is_omega2 = True
    from utils.screen_manager import print_screen, init_screen
    from utils.led_manager import init_led, blink_led
    from utils.buzzer_manager import init_buzzer, emit_beep
else:
    is_omega2 = False
    logging.info("Platform is not Omega2")

def process_notification(notification):
    """Create all type of notifications"""
    try:
        if create_file(notification):
            
            if is_omega2:
                # Print on screen only if this is the first notification
                if myconfig.SCREEN and count_files() == 1:
                    print_screen(notification)
                
                # make sound
                if myconfig.BUZZER: # and notification.sound
                    emit_beep()
            
                # turn on led
                if myconfig.LED: # and notification.light
                    blink_led()

    except IOError:
        raise IOError
    except:
        raise

def read_notification():
    """ Return the oldest notification. """
    try:
        notification = read_oldest_file()
    except IOError:
        raise IOError
    except:
        raise
    return notification
    
def delete_notification():
    """ Delete the oldest notification and print on the screen
        next one. 
    """
    try:
        deleted = delete_oldest_file()
    except:
        raise
    
    if is_omega2 and myconfig.SCREEN:
        #TODO clear screen
        # print on the screen the oldest following notif
        notification = read_oldest_file()
        if notification:
            print_screen(notification)
    return deleted

def init_hardware():
    """ Initialize the hardware part: screen, light, sound. """
    initialized = True
    
    if is_omega2:
        
        if myconfig.SCREEN:
            initialized = init_screen()
        
        if initialized and myconfig.SOUND:
            initialized = init_buzzer()
            
        if initialized and myconfig.LED:
            initialized = init_led()
    
    return initialized

