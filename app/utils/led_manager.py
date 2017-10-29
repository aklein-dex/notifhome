import onionGpio
import time
import thread
from config import config

PIN = config.PIN_LED

# specify sleep duration
sleepTime = 0.5

# instantiate a GPIO object
gpio_led = onionGpio.OnionGpio(PIN)
# set to output direction with zero (LOW) being the default value
gpio_led.setOutputDirection(0)


def init_led():
    """ Nothing special, just blink the led"""
    blink_led()
    return True

def blink_led():
    try:
       thread.start_new_thread( threaded_blink, () )
    except:
       print "Error: unable to start thread"
    
def threaded_blink():
    """ Blink led for a period of time"""
    # create a variable to hold the value of the LED
    ledValue = 1
    
    count = 0

    # TODO: a thread?
    while count < 6:
        # set the GPIO's value
        gpio_led.setValue(ledValue)

        # flip the value variable
        if ledValue == 1:
            ledValue = 0
        else:
            ledValue = 1

        # make the program pause
        time.sleep(sleepTime)
        count = count + 1
