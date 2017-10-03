import onionGpio
import time
from app.models.notification import Notification
from config import myconfig

PIN = myconfig.PIN_LED

# specify sleep duration
sleepTime = 0.5

# instantiate a GPIO object
gpio0 = onionGpio.OnionGpio(PIN)
# set to output direction with zero (LOW) being the default value
gpio0.setOutputDirection(0)


def init_led():
    """ Nothing special, just blink the led"""
    blink_led()
    return True
    
def blink_led():
    """ Blink led for a period of time"""
    # create a variable to hold the value of the LED
    ledValue = 1
    
    count = 0

    # TODO: a thread?
    while count < 6:
        # set the GPIO's value
        gpio0.setValue(ledValue)

        # flip the value variable
        if ledValue == 1:
            ledValue = 0
        else:
            ledValue = 1

        # make the program pause
        time.sleep(sleepTime)
        count = count + 1
